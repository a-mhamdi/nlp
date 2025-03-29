import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Creating a Document Corpus
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp](https://www.github.com/a-mhamdi/nlp)**
        """
    )
    return


@app.cell
def _():
    from gensim import corpora
    return (corpora,)


@app.cell
def _():
    # Sample documents
    documents = [
        "The quick brown fox jumps over the lazy dog",
        "Python is a great programming language",
        "Text processing with Gensim is efficient",
        "The lazy dog sleeps all day",
    ]
    return (documents,)


@app.cell
def _():
    # Tokenize documents
    def preprocess(text):
        # Convert to lowercase and split into words
        return text.lower().split()
    return (preprocess,)


@app.cell
def _(documents, preprocess):
    # Process all documents
    processed_docs = [preprocess(doc) for doc in documents]
    return (processed_docs,)


@app.cell
def _(corpora, processed_docs):
    # Create dictionary (maps words to IDs)
    dictionary = corpora.Dictionary(processed_docs)
    return (dictionary,)


@app.cell
def _(dictionary, processed_docs):
    # Convert documents to bag-of-words format
    corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
    return (corpus,)


@app.cell
def _(corpus, dictionary):
    print("Dictionary:", dictionary.token2id)
    print("\nFirst document BoW:", corpus[0])
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
