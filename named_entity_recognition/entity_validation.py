import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Entity Validation
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp](https://www.github.com/a-mhamdi/nlp)**
        """
    )
    return


@app.cell
def _():
    def validate_entities(entities, gazetteer):
        """
        Validate extracted entities against known lists
        """
        validated_entities = []

        for entity in entities:
            # Check against known entities
            if entity['text'] in gazetteer.get(entity['label'], []):
                entity['validated'] = True
            else:
                entity['validated'] = False
            validated_entities.append(entity)

        return validated_entities
    return (validate_entities,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
