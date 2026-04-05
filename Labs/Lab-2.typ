#import "Preamble.typ": *

#align(center)[
  #v(0.2em)
  #text(fill: dark, size: 18pt, weight: "bold")[Text Processing & Visualization Lab]
  #v(0.2em)
  #text(fill: teal, size: 10pt, style: "italic")[Full NLP Pipeline on Scientific Abstracts · Python + spaCy + GloVe]
  #v(0.1em)
  #line(length: 100%, stroke: 2pt + teal)
  #v(0.4em)
]

#grid(
  columns: (2fr, 1fr),
  gutter: 10pt,
  [*Students:* #h(1fr) #box(width: 8cm, line(length: 100%, stroke: 0.5pt + border))],
  [*Date:* #h(1fr) #box(width: 3cm, line(length: 100%, stroke: 0.5pt + border))],
)
#v(0.6em)

#block(
  width: 100%, fill: light, radius: 4pt,
  inset: (x: 12pt, y: 8pt),
  stroke: 1pt + border,
)[
  #text(weight: "bold", fill: dark)[Objective: ]
  #text(fill: gray)[This lab walks through an end-to-end NLP pipeline on PubMed abstracts — from spaCy tokenisation and TF-IDF scoring to GloVe document embeddings, dimensionality reduction, and a visualization dashboard exploring semantic structure across the corpus.]
]

#v(0.5em)

#q("1",
  [Use the NCBI eUtils API to fetch PubMed abstracts: call `esearch.fcgi` to retrieve IDs, then `efetch.fcgi` with a comma-joined ID list to get the content. Cache the result to a JSON file and load it into a pandas DataFrame with columns `id`, `title`, and `abstract`.],
  "Base URL: eutils.ncbi.nlm.nih.gov/entrez/eutils. Use ','.join(ids) for the id parameter. Cache with Path('cache.json'). Load with pd.DataFrame(json.loads(...))."
)

#q("2",
  [Process each abstract with spaCy (`en_core_web_sm`). Collect filtered lemmas (no stop words, punctuation, or whitespace) and extract named entities. Apply your function to the full DataFrame using `.apply()`.],
  "doc = nlp(text). Lemmas: [t.lemma_ for t in doc if not t.is_stop and not t.is_punct and not t.is_space]. Entities: [(e.text, e.label_) for e in doc.ents]."
)

#q("3",
  [Fit a `TfidfVectorizer` on the lemmatised abstracts. Retrieve the resulting matrix shape, explain what each cell represents, and extract the top 20 terms by mean TF-IDF score across all documents.],
  "Shape: (n_docs, n_features). Cell (i,j) = TF-IDF of term j in doc i. Top 20: np.asarray(matrix.mean(axis=0)).flatten().argsort()[::-1][:20]."
)

#q("4",
  [Load the `glove-twitter-25` model via gensim (set `GENSIM_DATA_DIR` before importing). For each abstract, filter lemmas present in the vocabulary and compute the mean word vector as the document embedding.],
  "Set os.environ['GENSIM_DATA_DIR'] before import. Filter: [w for w in lemmas if w in glove]. Embed: np.mean([glove[w] for w in filtered], axis=0)."
)

#q("5",
  [Reduce the 25-dim document embeddings to 2D: apply PCA first (10 components), then t-SNE. Store the resulting `x` and `y` coordinates back into the DataFrame.],
  "PCA first stabilises t-SNE. Use random_state=42 for reproducibility; perplexity must be less than n_samples. df['x'], df['y'] = X_2d[:,0], X_2d[:,1]."
)

#q("6",
  [Build a 2×2 matplotlib dashboard: a word cloud per keyword group (from `Counter` over all lemmas), and a t-SNE scatter plot with points coloured by document index. Save at 150 DPI with tight bounding box.],
  "fig, axes = plt.subplots(2,2,figsize=(16,12)). WordCloud: ax.imshow(wc); ax.axis('off'). Scatter: ax.scatter(x,y,c=range(n),cmap='viridis'). Save: plt.savefig(...,dpi=150,bbox_inches='tight')."
)

#v(0.6em)

#line(length: 100%, stroke: 1pt + border)