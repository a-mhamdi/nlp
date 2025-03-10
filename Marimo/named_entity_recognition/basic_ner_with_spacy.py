import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Basic NER with Spacy
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp-workshop](https://www.github.com/a-mhamdi/nlp-workshop)**
        """
    )
    return


@app.cell
def _():
    import spacy
    return (spacy,)


@app.cell
def _(spacy):
    # Load English language model
    nlp = spacy.load("en_core_web_sm")
    return (nlp,)


@app.cell
def _(nlp):
    def spacy_ner(text):
        """
        Perform NER using spaCy
        """
        # Process text
        doc = nlp(text)

        # Extract entities
        entities = [
            {
                'text': ent.text,
                'label': ent.label_,
                'start': ent.start_char,
                'end': ent.end_char
            }
            for ent in doc.ents
        ]

        return entities
    return (spacy_ner,)


@app.cell
def _(spacy_ner):
    # Example usage
    if __name__ == "__main__":
        text = "Microsoft's CEO Satya Nadella visited London last week."
        entities = spacy_ner(text)

        for entity in entities:
            print(f"Entity: {entity['text']}")
            print(f"Type: {entity['label']}")
            print(f"Position: {entity['start']}-{entity['end']}\n")
    return entities, entity, text


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
