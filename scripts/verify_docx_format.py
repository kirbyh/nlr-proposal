"""
verify_docx_format.py — Programmatic format verification for draft.docx

Checks:
  1. Page size = Letter, margins = 1 inch
  2. Normal style = TNR 12pt, double-spaced, justified
  3. Heading styles = bold TNR 12pt
  4. Sample paragraphs have correct font/spacing
  5. Subscript rendering = native Word (not Unicode glyphs)
  6. Math = OMML blocks present
  7. Tables present
  8. Title page = centered + bold first paragraph
  9. Line numbers configured
  10. Page numbers in footer

Output: PASS/FAIL/WARN checklist.
"""

import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn


def approx_inches(emu, target_inches, tolerance=0.05):
    """Check if EMU value is approximately target_inches."""
    target_emu = int(target_inches * 914400)
    return abs(emu - target_emu) < int(tolerance * 914400)


def check_page_setup(doc, results):
    """Check page size and margins."""
    section = doc.sections[0]

    # Page size
    if approx_inches(section.page_width, 8.5) and approx_inches(section.page_height, 11):
        results.append(("PASS", "Page size", "Letter (8.5 x 11 in)"))
    else:
        w = section.page_width / 914400
        h = section.page_height / 914400
        results.append(("FAIL", "Page size", f"Got {w:.1f} x {h:.1f} in, expected 8.5 x 11"))

    # Margins
    margins_ok = all([
        approx_inches(section.top_margin, 1),
        approx_inches(section.bottom_margin, 1),
        approx_inches(section.left_margin, 1),
        approx_inches(section.right_margin, 1),
    ])
    if margins_ok:
        results.append(("PASS", "Margins", "1 inch all sides"))
    else:
        results.append(("FAIL", "Margins", "Not all margins are 1 inch"))


def check_normal_style(doc, results):
    """Check Normal style properties."""
    style = doc.styles["Normal"]
    font = style.font

    # Font name
    if font.name == "Times New Roman":
        results.append(("PASS", "Normal font", "Times New Roman"))
    else:
        results.append(("FAIL", "Normal font", f"Got '{font.name}', expected 'Times New Roman'"))

    # Font size
    if font.size == Pt(12):
        results.append(("PASS", "Normal size", "12pt"))
    else:
        sz = font.size / 12700 if font.size else "None"
        results.append(("FAIL", "Normal size", f"Got {sz}pt, expected 12pt"))

    # Spacing (check XML for line=480)
    ppr = style.element.find(qn("w:pPr"))
    if ppr is not None:
        spacing = ppr.find(qn("w:spacing"))
        if spacing is not None:
            line_val = spacing.get(qn("w:line"))
            if line_val == "480":
                results.append(("PASS", "Normal spacing", "Double-spaced (480 twips)"))
            else:
                results.append(("FAIL", "Normal spacing", f"Line spacing = {line_val}, expected 480"))
        else:
            results.append(("WARN", "Normal spacing", "No spacing element found in Normal style"))
    else:
        results.append(("WARN", "Normal spacing", "No pPr found in Normal style"))

    # Alignment
    alignment = style.paragraph_format.alignment
    if alignment == WD_ALIGN_PARAGRAPH.JUSTIFY:
        results.append(("PASS", "Normal alignment", "Justified"))
    else:
        results.append(("WARN", "Normal alignment", f"Got {alignment}, expected JUSTIFY"))


def check_heading_styles(doc, results):
    """Check Heading 1 and 2 styles."""
    for name in ["Heading 1", "Heading 2"]:
        try:
            style = doc.styles[name]
            font = style.font
            if font.name == "Times New Roman" and font.bold:
                results.append(("PASS", f"{name} style", "TNR Bold"))
            else:
                results.append(("FAIL", f"{name} style",
                                f"Font='{font.name}', Bold={font.bold}"))
            if font.color and font.color.rgb:
                from docx.shared import RGBColor
                if font.color.rgb == RGBColor(0, 0, 0):
                    results.append(("PASS", f"{name} color", "Black"))
                else:
                    results.append(("WARN", f"{name} color",
                                    f"Color={font.color.rgb}, expected black"))
        except KeyError:
            results.append(("FAIL", f"{name} style", "Style not found"))


def check_sample_paragraphs(doc, results):
    """Spot-check actual paragraph formatting in the document body."""
    body_paras = [p for p in doc.paragraphs if p.text.strip() and len(p.text) > 50]
    if not body_paras:
        results.append(("WARN", "Sample paragraphs", "No substantial paragraphs found"))
        return

    # Check first 3 body paragraphs
    checked = 0
    tnr_count = 0
    for p in body_paras[:5]:
        for run in p.runs:
            if run.font.name == "Times New Roman" or run.font.name is None:
                # None means inherited from style
                tnr_count += 1
            checked += 1
            break  # Check first run only

    if checked > 0:
        if tnr_count == checked:
            results.append(("PASS", "Body paragraph fonts", f"{tnr_count}/{checked} paragraphs use TNR (or inherited)"))
        else:
            results.append(("WARN", "Body paragraph fonts", f"{tnr_count}/{checked} paragraphs use TNR"))
    else:
        results.append(("WARN", "Body paragraph fonts", "No runs to check"))


def check_unicode_subscripts(doc, results):
    """Check that Unicode sub/superscript chars have been converted to native Word formatting."""
    unicode_sub = set("₀₁₂₃₄₅₆₇₈₉")
    unicode_sup = set("⁰¹²³⁴⁵⁶⁷⁸⁹")
    all_special = unicode_sub | unicode_sup

    found_unicode = []
    found_native_sub = 0
    found_native_sup = 0

    for p in doc.paragraphs:
        for run in p.runs:
            text = run.text
            for ch in text:
                if ch in all_special:
                    found_unicode.append(ch)
            # Check for native sub/superscript via XML
            rpr = run._r.find(qn("w:rPr"))
            if rpr is not None:
                if rpr.find(qn("w:vertAlign")) is not None:
                    va = rpr.find(qn("w:vertAlign"))
                    val = va.get(qn("w:val"))
                    if val == "subscript":
                        found_native_sub += 1
                    elif val == "superscript":
                        found_native_sup += 1

    if found_unicode:
        results.append(("FAIL", "Unicode sub/superscripts",
                        f"Found {len(found_unicode)} unconverted Unicode chars: "
                        f"{''.join(sorted(set(found_unicode)))}"))
    else:
        results.append(("PASS", "Unicode sub/superscripts", "No unconverted Unicode chars found"))

    if found_native_sub > 0 or found_native_sup > 0:
        results.append(("PASS", "Native sub/superscripts",
                        f"{found_native_sub} subscript + {found_native_sup} superscript runs"))
    else:
        results.append(("WARN", "Native sub/superscripts", "No native sub/superscript runs found"))


def check_math(doc, results):
    """Check for OMML math blocks."""
    body = doc.element.body
    math_elements = body.findall(".//" + qn("m:oMathPara")) + body.findall(".//" + qn("m:oMath"))
    if math_elements:
        results.append(("PASS", "Math (OMML)", f"{len(math_elements)} math elements found"))
    else:
        results.append(("WARN", "Math (OMML)", "No OMML math found (may use text fallback)"))


def check_tables(doc, results):
    """Check that tables are present."""
    n = len(doc.tables)
    if n > 0:
        results.append(("PASS", "Tables", f"{n} table(s) found"))
    else:
        results.append(("WARN", "Tables", "No tables found"))


def check_title_page(doc, results):
    """Check that first paragraph is centered and bold (title)."""
    if not doc.paragraphs:
        results.append(("FAIL", "Title page", "No paragraphs"))
        return

    first = doc.paragraphs[0]
    style_name = first.style.name if first.style else ""

    # Check alignment - direct or inherited from style
    align = first.paragraph_format.alignment
    style_align = first.style.paragraph_format.alignment if first.style else None
    centered = (align == WD_ALIGN_PARAGRAPH.CENTER or
                style_align == WD_ALIGN_PARAGRAPH.CENTER)

    # Check bold - direct on runs or inherited from style
    has_bold = any(run.bold for run in first.runs if run.text.strip())
    style_bold = first.style.font.bold if first.style else False
    has_bold = has_bold or style_bold

    detail = f"Style='{style_name}'"
    if centered and has_bold:
        results.append(("PASS", "Title page", f"Centered + bold ({detail})"))
    elif centered:
        results.append(("WARN", "Title page", f"Centered but not bold ({detail})"))
    elif style_name in ("Title", "Author"):
        # Custom style applied - formatting comes from reference.docx
        results.append(("PASS", "Title page", f"Custom style '{style_name}' applied (formatting from reference.docx)"))
    elif has_bold:
        results.append(("WARN", "Title page", f"Bold but not centered ({detail})"))
    else:
        results.append(("WARN", "Title page", f"Alignment={align}, Bold={has_bold} ({detail})"))


def check_line_numbers(doc, results):
    """Check for line number configuration in section properties."""
    found = False
    for section in doc.sections:
        sectPr = section._sectPr
        ln_num = sectPr.find(qn("w:lnNumType"))
        if ln_num is not None:
            found = True
            break
    if found:
        results.append(("PASS", "Line numbers", "lnNumType found in section properties"))
    else:
        results.append(("WARN", "Line numbers",
                        "No lnNumType in section properties (may need manual: Layout > Line Numbers)"))


def check_page_numbers(doc, results):
    """Check for page number fields in footer."""
    found = False
    for section in doc.sections:
        try:
            footer = section.footer
            for p in footer.paragraphs:
                for run in p.runs:
                    # Check for PAGE field
                    fld_chars = run._r.findall(qn("w:fldChar"))
                    instr_texts = run._r.findall(qn("w:instrText"))
                    if fld_chars or instr_texts:
                        found = True
                        break
                # Also check paragraph XML directly
                xml = p._element.xml
                if "PAGE" in xml:
                    found = True
        except Exception:
            pass
    if found:
        results.append(("PASS", "Page numbers", "PAGE field found in footer"))
    else:
        results.append(("WARN", "Page numbers",
                        "No PAGE field in footer (may need manual: Insert > Page Number)"))


def main():
    repo = Path(__file__).resolve().parent.parent
    docx_path = repo / "manuscript" / "draft.docx"

    if not docx_path.exists():
        print(f"ERROR: {docx_path} not found. Run export first.")
        sys.exit(1)

    doc = Document(str(docx_path))
    results = []

    check_page_setup(doc, results)
    check_normal_style(doc, results)
    check_heading_styles(doc, results)
    check_sample_paragraphs(doc, results)
    check_unicode_subscripts(doc, results)
    check_math(doc, results)
    check_tables(doc, results)
    check_title_page(doc, results)
    check_line_numbers(doc, results)
    check_page_numbers(doc, results)

    # Print results
    print("\n=== DOCX Format Verification ===\n")
    passes = fails = warns = 0
    for status, check, detail in results:
        icon = {"PASS": "PASS", "FAIL": "FAIL", "WARN": "WARN"}[status]
        print(f"  [{icon}] {check}: {detail}")
        if status == "PASS":
            passes += 1
        elif status == "FAIL":
            fails += 1
        else:
            warns += 1

    print(f"\n  Summary: {passes} PASS, {fails} FAIL, {warns} WARN")
    print(f"  File: {docx_path}")

    if fails > 0:
        print("\n  STATUS: ISSUES FOUND — review FAIL items above")
        sys.exit(1)
    elif warns > 0:
        print("\n  STATUS: MOSTLY OK — review WARN items above")
        sys.exit(0)
    else:
        print("\n  STATUS: ALL CHECKS PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
