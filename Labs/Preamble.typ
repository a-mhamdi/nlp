#let dark    = rgb("#1A1A2E")
#let green   = rgb("#2D6A4F")
#let teal    = rgb("#40916C")
#let light   = rgb("#D8F3DC")
#let border  = rgb("#B7E4C7")
#let codebg  = rgb("#F0F4F0")
#let gray    = rgb("#4A5568")
#let white   = rgb("#FFFFFF")

#set page(
  paper: "a4",
  margin: (top: 1.8cm, bottom: 1.8cm, left: 1.8cm, right: 1.8cm),
)
#set text(font: "Alegreya", size: 10pt, fill: gray)
#set par(justify: true, leading: 0.65em)

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

#let hint(body) = block(
  width: 100%,
  fill: codebg,
  radius: 3pt,
  inset: (x: 10pt, y: 7pt),
  stroke: (left: 3pt + teal),
  stack(spacing: 3pt,
    text(fill: teal, size: 8.5pt,weight: "bold", "💡 Hint"),
    v(0.8em),
    text(fill: gray, size: 8.5pt, body)
  )
)

#let q(n, question, h) = {
  v(0.25em)
  grid(
    columns: (0.55cm, 1fr),
    gutter: 6pt,
    text(fill: teal, weight: "bold", size: 10pt, [#n.]),
    stack(spacing: 5pt,
      text(fill: dark, size: 10pt, question),
      hint(h)
    )
  )
  v(0.15em)
}