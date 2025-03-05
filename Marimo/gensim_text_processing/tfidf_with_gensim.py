import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # TFIDF with Gensim
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp](https://www.github.com/a-mhamdi/nlp)**
        """
    )
    return


@app.cell
def _():
    from gensim import corpora, models
    from LOCAL.creating_a_document_corpus import preprocess
    return corpora, models, preprocess


@app.cell
def _(corpora, models, preprocess):
    def create_tfidf_model(documents):
        """
        Create a TF-IDF model from a list of documents
        """
        # Preprocess documents
        processed_docs = [preprocess(doc) for doc in documents]

        # Create dictionary
        dictionary = corpora.Dictionary(processed_docs)

        # Create BOW corpus
        bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

        # Create TF-IDF model
        tfidf_model = models.TfidfModel(bow_corpus)

        # Transform corpus to TF-IDF space
        corpus_tfidf = tfidf_model[bow_corpus]

        return dictionary, tfidf_model, corpus_tfidf
    return (create_tfidf_model,)


@app.cell
def _(create_tfidf_model):
    if __name__ == '__main__':
        docs = [
            "Machine learning is fascinating",
            "Deep learning is a subset of machine learning",
            "Neural networks are used in deep learning",
            "Python is great for machine learning"
        ]

        dictionary, tfidf_model, corpus_tfidf = create_tfidf_model(docs)

        # Print TF-IDF scores for each document
        for i, doc in enumerate(corpus_tfidf):
            print(f"\nDocument {i+1} TF-IDF scores:")
            for id, score in doc:
                print(f"Word: {dictionary[id]}, Score: {score:.4f}")
    return corpus_tfidf, dictionary, doc, docs, i, id, score, tfidf_model


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
