#import "Preamble.typ": *

#align(center)[
  #v(0.2em)
  #text(fill: dark, size: 18pt, weight: "bold")[Regex & Regex-based Tokenisation]
  #v(0.2em)
  #text(fill: teal, size: 10pt, style: "italic")[
    Pattern Matching · Custom Tokenisers · Scientific Text · Python `re` module
  ]
  #v(0.1em)
  #line(length: 100%, stroke: 2pt + teal)
  #v(0.4em)
]

#grid(columns: (2fr, 1fr),
  gutter: 10pt,
  [*Students:* #h(1fr) #box(width: 8cm, line(length: 100%, stroke: 0.5pt + border))],
  [*Date:* #h(1fr) #box(width: 3cm, line(length: 100%, stroke: 0.5pt + border))],
)
#v(0.6em)

#block(width: 100%, fill: light, radius: 4pt, inset: (x: 12pt, y: 8pt), stroke: 1pt + border)[
  #text(weight: "bold", fill: dark)[Objective: ]
  #text(fill: gray)[
    This lab covers regular expressions as a practical tool for scientific text processing — from basic pattern matching to building a custom tokeniser that handles domain-specific notation.
  ]
]

#v(0.5em)

#q("1",
  [Scientific abstracts contain values like `37.5°C`, `1.2 µM`, `p < 0.001`. Write a single regex capturing a numeric value followed by an optional space and a unit abbreviation (letters, Greek letters, `%`, `°`). Test with `re.findall()`.],
  "Use \\d+(?:\\.\\d+)? for the number, \\s? for the space, [\\w°µ%]+ for the unit.",
)

#q("2",
  [Citations appear as `[1]`, `[1–3]`, or `(Smith et al., 2019)`. Write two patterns — bracket-style and author-year — then merge them with alternation into one compiled pattern.],
  "Bracket: \\[\\d+(?:[,–]\\d+)*\\]. Author-year: \\((?:[A-Z][a-z]+ et al\\.\\s)?\\d{4}\\). Combine with | in re.compile(); use re.UNICODE."
)

#q("3",
  [Write a negative lookbehind preventing sentence splits after abbreviations like `et al.`, `Fig.`, `vs.`. Explain the difference from a negative lookahead.],
  "(?<!\\b(?:et al|Fig|cf|vs))\\.\\s+[A-Z]. A lookbehind checks what precedes; a lookahead checks what follows — neither consumes characters.",
)

#q("4",
  [Write a three-stage normalisation function using `re.sub()`: (1) strip HTML/XML tags, (2) decode common entities (`&amp;`, `&#x03B1;`), (3) collapse whitespace.],
  "Stage 1: re.sub(r'<[^>]+>', '', text). Stage 2: dict + lambda. Stage 3: re.sub(r'\\s+', ' ', text).strip(). Strip tags before decoding entities.",
)

#q("5",
  [Implement a `RegexTokeniser` class with types in priority order: CITATION, FORMULA, MEASUREMENT, ABBREV, WORD, NUMBER, PUNCT. The `tokenise(text)` method returns `(type, value)` tuples.],
  "Use named groups (?P<TYPE>...) joined with |. In tokenise(), use re.finditer(); read match.lastgroup and match.group(). Drop WHITESPACE tokens.",
)

#v(0.6em)

#line(length: 100%, stroke: 1pt + border)