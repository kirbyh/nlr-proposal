"""
Generate a reference.docx for Pandoc that matches journal formatting:
  - Times New Roman 12pt throughout
  - Double-spaced
  - 1-inch margins, Letter size
  - Page numbers bottom-right
  - Line numbers continuous (via XML injection)
  - Justified body text, left-aligned headings

Customize the formatting in generate_reference_docx() for your target journal.
"""

import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml


def set_font(style, name="Times New Roman", size=12, bold=False, italic=False):
    """Set font properties on a style."""
    font = style.font
    font.name = name
    font.size = Pt(size)
    font.bold = bold
    font.italic = italic
    font.color.rgb = RGBColor(0, 0, 0)
    # Set East Asian and complex script fonts AND remove theme font overrides
    rpr = style.element.get_or_add_rPr()
    elem = rpr.find(qn("w:rFonts"))
    if elem is None:
        elem = parse_xml(f'<w:rFonts {nsdecls("w")}/>')
        rpr.append(elem)
    elem.set(qn("w:ascii"), name)
    elem.set(qn("w:hAnsi"), name)
    elem.set(qn("w:eastAsia"), name)
    elem.set(qn("w:cs"), name)
    # Remove theme font attributes so explicit font name takes precedence
    for attr in ["asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"]:
        key = qn(f"w:{attr}")
        if key in elem.attrib:
            del elem.attrib[key]


def set_spacing(style, before=0, after=0, line=480):
    """Set paragraph spacing. line=480 = double space (240 twips per line)."""
    pf = style.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing_rule = None  # Clear any rule
    # Set exact line spacing via XML for reliability
    ppr = style.element.get_or_add_pPr()
    spacing = ppr.find(qn("w:spacing"))
    if spacing is None:
        spacing = parse_xml(f'<w:spacing {nsdecls("w")}/>')
        ppr.append(spacing)
    spacing.set(qn("w:line"), str(line))
    spacing.set(qn("w:lineRule"), "auto")
    spacing.set(qn("w:before"), str(int(before * 20)))  # Pt to twips
    spacing.set(qn("w:after"), str(int(after * 20)))


def set_alignment(style, alignment):
    """Set paragraph alignment."""
    style.paragraph_format.alignment = alignment


def override_theme_fonts(doc, name="Times New Roman"):
    """Override the document theme's major and minor fonts to TNR.

    Pandoc 3.7+ ships Aptos/Aptos Display as theme fonts. Word resolves
    theme font references (asciiTheme, hAnsiTheme) at render time, so
    even if we set explicit font names on styles, theme references win.
    This function patches the theme XML so the theme itself uses TNR.
    """
    from docx.opc.constants import RELATIONSHIP_TYPE as RT
    import zipfile
    import io

    # Access the theme part via the document's package
    try:
        theme_part = doc.part.package.part_related_by(
            "http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme"
        )
    except Exception:
        # If no theme relationship, try via main document part
        try:
            for rel in doc.part.rels.values():
                if "theme" in rel.reltype:
                    theme_part = rel.target_part
                    break
            else:
                return  # No theme found
        except Exception:
            return

    from lxml import etree
    theme_xml = etree.fromstring(theme_part.blob)
    ns = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}

    # Override majorFont (headings) and minorFont (body)
    for font_scheme in ["majorFont", "minorFont"]:
        elem = theme_xml.find(f".//a:{font_scheme}", ns)
        if elem is not None:
            for child_tag in ["latin", "ea", "cs"]:
                child = elem.find(f"a:{child_tag}", ns)
                if child is not None:
                    child.set("typeface", name)

    theme_part._blob = etree.tostring(theme_xml, xml_declaration=True,
                                       encoding="UTF-8", standalone=True)


def add_line_numbers(doc):
    """Add continuous line numbers to all sections via XML."""
    for section in doc.sections:
        sectPr = section._sectPr
        # Remove existing lnNumType if present
        for ln in sectPr.findall(qn("w:lnNumType")):
            sectPr.remove(ln)
        # Add continuous line numbering
        ln_num = parse_xml(
            f'<w:lnNumType {nsdecls("w")} '
            f'w:countBy="1" w:restart="continuous" w:distance="360"/>'
        )
        sectPr.append(ln_num)


def add_page_numbers(doc):
    """Add page numbers to bottom-right of footer."""
    for section in doc.sections:
        footer = section.footer
        footer.is_linked_to_previous = False
        # Clear existing footer content
        for p in footer.paragraphs:
            p.clear()

        # Use the first paragraph (always exists)
        p = footer.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

        # Set font for footer
        run = p.add_run()
        run.font.name = "Times New Roman"
        run.font.size = Pt(12)

        # Add PAGE field code
        fld_char_begin = parse_xml(
            f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>'
        )
        run._r.append(fld_char_begin)

        instr = parse_xml(
            f'<w:instrText {nsdecls("w")} xml:space="preserve"> PAGE </w:instrText>'
        )
        run._r.append(instr)

        fld_char_end = parse_xml(
            f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>'
        )
        run._r.append(fld_char_end)


def generate_reference_docx(output_path):
    """Generate a fresh reference.docx with journal formatting."""

    # Start from Pandoc's default reference doc for maximum compatibility
    tmp_path = output_path.parent / "_pandoc_default_reference.docx"
    subprocess.run(
        ["pandoc", "-o", str(tmp_path), "--print-default-data-file",
         "reference.docx"],
        capture_output=True,
    )

    # If pandoc extraction worked, use it; otherwise start fresh
    if tmp_path.exists() and tmp_path.stat().st_size > 0:
        doc = Document(str(tmp_path))
        tmp_path.unlink()
    else:
        # Fallback: extract via pandoc --print-default-data-file
        result = subprocess.run(
            ["pandoc", "--print-default-data-file", "reference.docx"],
            capture_output=True,
        )
        if result.returncode == 0 and len(result.stdout) > 0:
            tmp_path.write_bytes(result.stdout)
            doc = Document(str(tmp_path))
            tmp_path.unlink()
        else:
            doc = Document()

    # --- Page Setup ---
    for section in doc.sections:
        section.page_width = Inches(8.5)
        section.page_height = Inches(11)
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # --- Style Configuration ---
    styles = doc.styles

    # Normal (body text)
    normal = styles["Normal"]
    set_font(normal, bold=False)
    set_spacing(normal, before=0, after=0, line=480)
    set_alignment(normal, WD_ALIGN_PARAGRAPH.JUSTIFY)

    # Heading 1
    try:
        h1 = styles["Heading 1"]
    except KeyError:
        h1 = styles.add_style("Heading 1", 1)  # paragraph style
    set_font(h1, bold=True)
    set_spacing(h1, before=0, after=0, line=480)
    set_alignment(h1, WD_ALIGN_PARAGRAPH.LEFT)
    h1.font.color.rgb = RGBColor(0, 0, 0)

    # Heading 2
    try:
        h2 = styles["Heading 2"]
    except KeyError:
        h2 = styles.add_style("Heading 2", 1)
    set_font(h2, bold=True)
    set_spacing(h2, before=0, after=0, line=480)
    set_alignment(h2, WD_ALIGN_PARAGRAPH.LEFT)
    h2.font.color.rgb = RGBColor(0, 0, 0)

    # Heading 3
    try:
        h3 = styles["Heading 3"]
    except KeyError:
        h3 = styles.add_style("Heading 3", 1)
    set_font(h3, bold=True, italic=True)
    set_spacing(h3, before=0, after=0, line=480)
    set_alignment(h3, WD_ALIGN_PARAGRAPH.LEFT)
    h3.font.color.rgb = RGBColor(0, 0, 0)

    # Title
    try:
        title = styles["Title"]
    except KeyError:
        title = styles.add_style("Title", 1)
    set_font(title, bold=True)
    set_spacing(title, before=0, after=0, line=480)
    set_alignment(title, WD_ALIGN_PARAGRAPH.CENTER)
    title.font.color.rgb = RGBColor(0, 0, 0)

    # Author (Pandoc uses "Author" style for YAML author field)
    try:
        author = styles["Author"]
    except KeyError:
        author = styles.add_style("Author", 1)
    set_font(author, bold=False)
    set_spacing(author, before=0, after=0, line=480)
    set_alignment(author, WD_ALIGN_PARAGRAPH.CENTER)

    # First Paragraph (Pandoc sometimes uses this)
    try:
        fp = styles["First Paragraph"]
        set_font(fp, bold=False)
        set_spacing(fp, before=0, after=0, line=480)
        set_alignment(fp, WD_ALIGN_PARAGRAPH.JUSTIFY)
    except KeyError:
        pass

    # Body Text
    try:
        bt = styles["Body Text"]
        set_font(bt, bold=False)
        set_spacing(bt, before=0, after=0, line=480)
        set_alignment(bt, WD_ALIGN_PARAGRAPH.JUSTIFY)
    except KeyError:
        pass

    # Table styles - set font but keep single spacing for readability
    for table_style_name in [
        "Compact", "Table", "Table Grid", "Table Normal",
    ]:
        try:
            ts = styles[table_style_name]
            set_font(ts, bold=False)
        except KeyError:
            pass

    # --- Override Theme Fonts ---
    # Pandoc 3.7+ uses Aptos as theme font; override to TNR
    override_theme_fonts(doc)

    # --- Line Numbers ---
    add_line_numbers(doc)

    # --- Page Numbers ---
    add_page_numbers(doc)

    # --- Clear body content (reference doc should be minimal) ---
    # Keep only one empty paragraph
    for i, p in enumerate(doc.paragraphs):
        if i == 0:
            p.text = ""
            p.style = normal
        else:
            p._element.getparent().remove(p._element)

    # Save
    doc.save(str(output_path))
    print(f"Generated: {output_path}")
    print("  - Times New Roman 12pt, double-spaced, justified")
    print("  - 1-inch margins, Letter size")
    print("  - Page numbers (bottom-right)")
    print("  - Line numbers (continuous)")


if __name__ == "__main__":
    repo = Path(__file__).resolve().parent.parent
    output = repo / "manuscript" / "reference.docx"
    generate_reference_docx(output)
