# Obsidian Integration

The user maintains research notes in an Obsidian vault. These notes serve as reference material for manuscript writing.

---

## Rules

1. **Notes are reference, not infallible.** Obsidian notes represent the user's working understanding at time of writing. They may contain:
   - Preliminary interpretations that evolved
   - Rough calculations that were later refined
   - Notes from papers that may have been misread initially

2. **Flag contradictions.** If an Obsidian note contradicts a primary source (paper PDF, verified calculation, or LES data), flag it clearly:
   ```
   NOTE CONTRADICTION: Obsidian note "[note name]" says X, but [primary source] shows Y.
   Recommend updating the Obsidian note after confirming.
   ```

3. **Append-only writes.** When writing back to the Obsidian vault:
   - ONLY append to existing notes (add content at the end)
   - NEVER overwrite, restructure, rename, or delete notes
   - Use a clear delimiter when appending:
     ```
     ---
     ## Claude Code Addition (YYYY-MM-DD)
     [content]
     ```

4. **Vault path:** Stored in `.claude/state/external-repos.json` (set via `/onboard`). If not set, ask the user.

5. **Link format:** When referencing Obsidian notes in the manuscript workflow, use the note title, not filesystem paths (Obsidian uses `[[wikilinks]]` internally).
