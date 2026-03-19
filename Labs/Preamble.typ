// ── Colors ────────────────────────────────────────────────────────────────────
#let dark    = rgb("#1A1A2E")
#let green   = rgb("#2D6A4F")
#let teal    = rgb("#40916C")
#let light   = rgb("#D8F3DC")
#let border  = rgb("#B7E4C7")
#let codebg  = rgb("#F0F4F0")
#let gray    = rgb("#4A5568")
#let white   = rgb("#FFFFFF")
#let orange  = rgb("#C05621")
#let orangebg = rgb("#FFFAF0")

// ── Page setup ────────────────────────────────────────────────────────────────
#set page(
  paper: "a4",
  margin: (top: 1.8cm, bottom: 1.8cm, left: 1.8cm, right: 1.8cm),
)
#set text(font: "Alegreya", size: 10pt, fill: gray)
#set par(justify: true, leading: 0.65em)

// ── Heading styles ────────────────────────────────────────────────────────────
#show heading.where(level: 1): it => {
  v(0.6em)
  block(
    width: 100%,
    stroke: (bottom: 2pt + teal),
    inset: (bottom: 4pt),
    text(fill: dark, size: 13pt, weight: "bold", it.body)
  )
  v(0.3em)
}

#show heading.where(level: 2): it => {
  v(0.4em)
  text(fill: green, size: 11pt, weight: "bold", it.body)
  v(0.2em)
}

// ── Components ────────────────────────────────────────────────────────────────

#let step-box(num, title, desc) = block(
  width: 100%,
  radius: 4pt,
  clip: true,
  stroke: 1pt + border,
  grid(
    columns: (1.4cm, 1fr),
    rows: auto,
    block(
      width: 100%, height: 100%,
      fill: green,
      inset: (x: 6pt, y: 10pt),
      align(center + horizon,
        text(fill: white, size: 16pt, weight: "bold", num)
      )
    ),
    block(
      width: 100%,
      fill: light,
      inset: (x: 10pt, y: 8pt),
      stack(spacing: 3pt,
        text(fill: dark, size: 11pt, weight: "bold", title),
        text(fill: gray, size: 9pt, desc),
      )
    )
  )
)

#let hint(body) = block(
  width: 100%,
  fill: codebg,
  radius: 3pt,
  inset: (x: 10pt, y: 7pt),
  stroke: (left: 3pt + teal),
  stack(spacing: 3pt,
    text(fill: teal, size: 8.5pt, weight: "bold", "💡 Hint"),
    text(fill: gray, size: 8.5pt, body)
  )
)

#let warn(body) = block(
  width: 100%,
  fill: orangebg,
  radius: 3pt,
  inset: (x: 10pt, y: 7pt),
  stroke: (left: 3pt + orange),
  stack(spacing: 3pt,
    text(fill: orange, size: 8.5pt, weight: "bold", "🔍 Think deeper"),
    text(fill: gray, size: 8.5pt, body)
  )
)

#let q(n, question, h, deeper: none) = {
  v(0.25em)
  grid(
    columns: (0.55cm, 1fr),
    gutter: 6pt,
    text(fill: teal, weight: "bold", size: 10pt, [#n.]),
    stack(spacing: 5pt,
      text(fill: dark, size: 10pt, question),
      hint(h),
      if deeper != none { warn(deeper) }
    )
  )
  v(0.15em)
}