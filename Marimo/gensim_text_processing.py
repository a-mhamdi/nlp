import marimo

__generated_with = "0.10.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Gensim Text Processing
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp](https://www.github.com/a-mhamdi/nlp)**
        """
    )
    return


@app.cell
def _():
    from gensim import corpora, models, similarities
    return corpora, models, similarities


@app.cell
def _(corpora, models, similarities):
    class GensimTextAnalyzer:
        def __init__(self):
            self.dictionary = None
            self.tfidf_model = None
            self.similarity_index = None

        def fit(self, documents):
            """Train the analyzer on a corpus of documents"""
            # Preprocess documents
            processed_docs = [doc.lower().split() for doc in documents]

            # Create dictionary
            self.dictionary = corpora.Dictionary(processed_docs)

            # Create BOW corpus
            bow_corpus = [self.dictionary.doc2bow(doc) for doc in processed_docs]

            # Create TF-IDF model
            self.tfidf_model = models.TfidfModel(bow_corpus)

            # Transform corpus to TF-IDF space
            corpus_tfidf = self.tfidf_model[bow_corpus]

            # Create similarity index
            self.similarity_index = similarities.MatrixSimilarity(corpus_tfidf)

        def get_similar_documents(self, query, top_n=5):
            """Find most similar documents to query"""
            # Process query
            query_bow = self.dictionary.doc2bow(query.lower().split())
            query_tfidf = self.tfidf_model[query_bow]

            # Compute similarities
            sims = self.similarity_index[query_tfidf]

            # Return top N similar documents
            return sorted(enumerate(sims), key=lambda x: x[1], reverse=True)[:top_n]
    return (GensimTextAnalyzer,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Create a `GensimTextAnalyzer` object""")
    return


@app.cell
def _(GensimTextAnalyzer):
    analyzer = GensimTextAnalyzer()
    return (analyzer,)


@app.cell
def _(analyzer):
    def find_similar(documents, query):
        """Find similar documents"""
        # Train analyzer
        analyzer.fit(documents)

        similar_docs = analyzer.get_similar_documents(query)

        print("\nMost similar documents to query:")
        for doc_id, score in similar_docs:
            print(f"Score: {score:.4f} - {documents[doc_id]}")
    return (find_similar,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Example #1""")
    return


@app.cell
def _(find_similar):
    documents_1 = [
        "The cat sits on the mat",
        "The dog runs in the park",
        "Cats and dogs are pets",
        "The mat is comfortable"
    ]

    query_1 = "Where is the cat sitting?"

    find_similar(documents_1, query_1)
    return documents_1, query_1


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Example #2""")
    return


@app.cell
def _(find_similar):
    documents_2 = [
            "Artificial intelligence is transforming industries",
            "Machine learning models need good data",
            "Deep learning requires powerful GPUs",
            "Data science combines statistics and programming",
            "Neural networks are inspired by biology"
        ]

    query_2 = "How is AI changing the world?"

    find_similar(documents_2, query_2)
    return documents_2, query_2


@app.cell
def _(mo):
    mo.md("""**Word Embeddings**""")
    return


@app.cell
def _():
    import gensim.downloader as api
    return (api,)


@app.cell
def _(api):
    model_glove_twitter = api.load("glove-twitter-25")
    return (model_glove_twitter,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Get word vectors""")
    return


@app.cell
def _(model_glove_twitter):
    vect_tn = model_glove_twitter['tunisia']
    print(vect_tn)
    return (vect_tn,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Find similar words""")
    return


@app.cell
def _(model_glove_twitter):
    similar_words = model_glove_twitter.most_similar("good")
    print(similar_words)
    return (similar_words,)


@app.cell
def _(model_glove_twitter):
    model_glove_twitter.doesnt_match(["free", "honest", "dignity", "microsoft"])
    return


@app.cell
def _(mo):
    mo.md("""King - Man = Queen - Woman""")
    return


@app.cell
def _(model_glove_twitter):
    model_glove_twitter.most_similar(positive=["king", "woman"], negative=["man"])[0:3]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""France - Paris = USA - Washington, D.C.""")
    return


@app.cell
def _(model_glove_twitter):
    model_glove_twitter.most_similar(positive=["france", "washington"], negative=["paris"])[0:3]
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
