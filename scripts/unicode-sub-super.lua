-- unicode-sub-super.lua
-- Pandoc Lua filter: convert Unicode sub/superscript characters to native
-- pandoc Subscript/Superscript elements so they render as Word formatting.
--
-- Handles consecutive runs: e.g., "¹⁵" -> Superscript("15")
-- Does not touch Math elements (separate AST nodes).

local sub_map = {
  ["\u{2080}"] = "0",
  ["\u{2081}"] = "1",
  ["\u{2082}"] = "2",
  ["\u{2083}"] = "3",
  ["\u{2084}"] = "4",
  ["\u{2085}"] = "5",
  ["\u{2086}"] = "6",
  ["\u{2087}"] = "7",
  ["\u{2088}"] = "8",
  ["\u{2089}"] = "9",
}

local sup_map = {
  ["\u{2070}"] = "0",
  ["\u{00B9}"] = "1",
  ["\u{00B2}"] = "2",
  ["\u{00B3}"] = "3",
  ["\u{2074}"] = "4",
  ["\u{2075}"] = "5",
  ["\u{2076}"] = "6",
  ["\u{2077}"] = "7",
  ["\u{2078}"] = "8",
  ["\u{2079}"] = "9",
}

-- Build a combined lookup: char -> {digit, type}
local char_info = {}
for c, d in pairs(sub_map) do
  char_info[c] = {digit = d, kind = "sub"}
end
for c, d in pairs(sup_map) do
  char_info[c] = {digit = d, kind = "sup"}
end

--- Process a Str element: split into runs of normal text,
--- subscript digits, and superscript digits.
local function process_str(el)
  local text = el.text
  local result = {}
  local buf = ""       -- buffer for normal text
  local spec_buf = ""  -- buffer for sub/super digits
  local spec_kind = nil  -- "sub" or "sup"

  -- Iterate over UTF-8 codepoints
  for pos, code in utf8.codes(text) do
    local char = utf8.char(code)
    local info = char_info[char]

    if info then
      -- This char is a sub or super digit
      if info.kind == spec_kind then
        -- Same kind as current run, extend
        spec_buf = spec_buf .. info.digit
      else
        -- Different kind or first special char
        -- Flush previous buffers
        if #buf > 0 then
          table.insert(result, pandoc.Str(buf))
          buf = ""
        end
        if #spec_buf > 0 then
          if spec_kind == "sub" then
            table.insert(result, pandoc.Subscript({pandoc.Str(spec_buf)}))
          else
            table.insert(result, pandoc.Superscript({pandoc.Str(spec_buf)}))
          end
          spec_buf = ""
        end
        spec_kind = info.kind
        spec_buf = info.digit
      end
    else
      -- Normal character
      -- Flush any pending special buffer
      if #spec_buf > 0 then
        if spec_kind == "sub" then
          table.insert(result, pandoc.Subscript({pandoc.Str(spec_buf)}))
        else
          table.insert(result, pandoc.Superscript({pandoc.Str(spec_buf)}))
        end
        spec_buf = ""
        spec_kind = nil
      end
      buf = buf .. char
    end
  end

  -- Flush remaining buffers
  if #spec_buf > 0 then
    if #buf > 0 then
      table.insert(result, pandoc.Str(buf))
      buf = ""
    end
    if spec_kind == "sub" then
      table.insert(result, pandoc.Subscript({pandoc.Str(spec_buf)}))
    else
      table.insert(result, pandoc.Superscript({pandoc.Str(spec_buf)}))
    end
  elseif #buf > 0 then
    table.insert(result, pandoc.Str(buf))
  end

  -- If nothing changed, return nil to keep original
  if #result == 1 and result[1].tag == "Str" and result[1].text == text then
    return nil
  end

  return result
end

-- Map of simple LaTeX math commands to Unicode replacements.
-- Only single-symbol math like $\pm$ is converted; complex expressions are left as OMML.
local simple_math_map = {
  ["\\pm"]     = "\u{00B1}",  -- ±
  ["\\mp"]     = "\u{2213}",  -- ∓
  ["\\times"]  = "\u{00D7}",  -- ×
  ["\\cdot"]   = "\u{00B7}",  -- ·
  ["\\approx"] = "\u{2248}",  -- ≈
  ["\\leq"]    = "\u{2264}",  -- ≤
  ["\\geq"]    = "\u{2265}",  -- ≥
  ["\\neq"]    = "\u{2260}",  -- ≠
  ["\\degree"] = "\u{00B0}",  -- °
  ["\\deg"]    = "\u{00B0}",  -- °
  ["\\alpha"]  = "\u{03B1}",  -- α
  ["\\beta"]   = "\u{03B2}",  -- β
  ["\\mu"]     = "\u{03BC}",  -- μ
  ["\\Delta"]  = "\u{0394}",  -- Δ
  ["\\delta"]  = "\u{03B4}",  -- δ
}

-- Filter: operate on Inline elements
function Str(el)
  local result = process_str(el)
  if result then
    return result
  end
end

--- Convert simple single-command InlineMath to Unicode text.
--- e.g., $\pm$ -> "±", but $K_\text{F}$ is left as math.
function Math(el)
  if el.mathtype ~= "InlineMath" then
    return nil
  end
  -- Strip surrounding whitespace
  local tex = el.text:match("^%s*(.-)%s*$")
  -- Check if it's a single simple command (with optional surrounding spaces)
  local replacement = simple_math_map[tex]
  if replacement then
    return pandoc.Str(replacement)
  end
  return nil
end
