import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


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


if __name__ == "__main__":
    app.run()
