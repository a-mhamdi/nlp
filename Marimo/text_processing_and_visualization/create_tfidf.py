import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Create TFIDF
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp](https://www.github.com/a-mhamdi/nlp)**
        """
    )
    return


@app.cell
def _():
    from sklearn.feature_extraction.text import TfidfVectorizer
    return (TfidfVectorizer,)


@app.cell
def _(TfidfVectorizer):
    def create_tfidf(documents):
        # Initialize TF-IDF vectorizer
        tfidf = TfidfVectorizer()
        # Create TF-IDF matrix
        X = tfidf.fit_transform(documents)
        # Get feature names
        feature_names = tfidf.get_feature_names_out()

        return X.toarray(), feature_names, tfidf
    return (create_tfidf,)


@app.cell
def _():
    if __name__ == '__main__':
        pass
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
