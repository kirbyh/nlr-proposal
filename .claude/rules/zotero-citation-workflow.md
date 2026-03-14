---
paths:
  - "manuscript/**/*.md"
  - "Bibliography_base.bib"
---

# Zotero-First Citation Workflow

All bibliography management goes through Zotero. Claude never adds entries directly to `Bibliography_base.bib`.

---

## Protocol

1. **Zotero is the single source of truth for references.** The user manages their Zotero library and exports to `Bibliography_base.bib`.

2. **When a citation is needed:**
   - Search `Bibliography_base.bib` for existing entries first.
   - If found: use the existing BibTeX key in the manuscript.
   - If NOT found: flag for the user with a clear message:
     ```
     CITATION NEEDED: [Author(s), Year, "Title fragment or topic"]
     Please add this to Zotero and re-export Bibliography_base.bib.
     ```

3. **Never fabricate BibTeX entries.** Do not create, guess, or approximate bibliography entries. Even if you know the paper details, the entry must come from Zotero to maintain library consistency.

4. **Citation format (Copernicus author-year):**
   - Narrative: `Smith et al. (2020)` or `Smith and Jones (2021)`
   - Parenthetical: `(Smith et al., 2020)` or `(Smith and Jones, 2021; Doe, 2019)`
   - In Markdown drafts, use: `[@Smith2020]` or `[@Smith2020; @Jones2021]` for Pandoc processing

5. **Batch flagging:** If multiple citations are needed in a section, collect them all and present a single list to the user rather than interrupting repeatedly.

6. **After user adds references:** Re-read `Bibliography_base.bib` before inserting citation keys — do not assume the key format.
