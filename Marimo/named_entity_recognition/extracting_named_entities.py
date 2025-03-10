import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Extracting Named Entities
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp-workshop](https://www.github.com/a-mhamdi/nlp-workshop)**
        """
    )
    return


@app.cell
def _():
    from LOCAL.basic_ner_with_nltk import nltk_ner
    return (nltk_ner,)


@app.cell
def _(nltk_ner):
    def extract_entities(text):
        """
        Extract and categorize named entities from text
        """
        entities = {
            'PERSON': [],
            'ORGANIZATION': [],
            'GPE': [],  # Geo-Political Entity
            'LOCATION': [],
            'DATE': [],
            'TIME': [],
            'MONEY': [],
            'PERCENT': []
        }

        # Get named entities
        named_entities = nltk_ner(text)

        # Extract entities
        for chunk in named_entities:
            if hasattr(chunk, 'label'):
                entity_name = ' '.join(c[0] for c in chunk)
                entity_type = chunk.label()
                if entity_type in entities:
                    entities[entity_type].append(entity_name)

        return entities
    return (extract_entities,)


@app.cell
def _(extract_entities):
    # Example usage
    if __name__ == "__main__":
        text = """
        Tim Cook, CEO of Apple Inc., announced yesterday that the company's revenue 
        grew by 15% to reach $365 billion in New York City.
        """

        entities = extract_entities(text)
        for entity_type, entity_list in entities.items():
            if entity_list:
                print(f"{entity_type}: {entity_list}")
    return entities, entity_list, entity_type, text


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
