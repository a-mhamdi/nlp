import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Create BoW
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp-workshop](https://www.github.com/a-mhamdi/nlp-workshop)**
        """
    )
    return


@app.cell
def _():
    from sklearn.feature_extraction.text import CountVectorizer
    return (CountVectorizer,)


@app.cell
def _(CountVectorizer):
    def create_bow(documents):
        # Initialize vectorizer
        vectorizer = CountVectorizer()
        # Create BOW representation
        X = vectorizer.fit_transform(documents)
        # Get feature names (vocabulary)
        feature_names = vectorizer.get_feature_names_out()
        # Convert to array
        bow_array = X.toarray()

        return bow_array, feature_names, vectorizer
    return (create_bow,)


@app.cell
def _(create_bow):
    # Example usage
    if __name__ == '__main__':
        documents = [
            "The cat sat on the mat",
            "The dog ran in the park",
            "The cat and dog played"
        ]

        bow_array, features, vectorizer = create_bow(documents)
        print("Features:", features)
        print("BOW Matrix:\n", bow_array)
    return bow_array, documents, features, vectorizer


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
