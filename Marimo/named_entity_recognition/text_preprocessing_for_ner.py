import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Text Preprocessing for NER
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp-workshop](https://www.github.com/a-mhamdi/nlp-workshop)**
        """
    )
    return


@app.cell
def _(re):
    def preprocess_for_ner(text):
        """
        Preprocess text for better NER results
        """
        # Convert to proper case (helps with name recognition)
        text = text.title()

        # Handle special characters
        text = re.sub(r'[^\w\s.,!?-]', ' ', text)

        # Normalize whitespace
        text = ' '.join(text.split())

        return text
    return (preprocess_for_ner,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
