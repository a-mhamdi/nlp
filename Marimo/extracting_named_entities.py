import marimo

__generated_with = "0.12.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Extracting Named Entities
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp](https://www.github.com/a-mhamdi/nlp)**
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## NER using NLTK""")
    return


@app.cell
def _():
    import nltk
    return (nltk,)


@app.cell
def _():
    from nltk import ne_chunk
    from nltk import word_tokenize, pos_tag
    return ne_chunk, pos_tag, word_tokenize


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Download required NLTK data""")
    return


@app.cell
def _(nltk):
    nltk.download('averaged_perceptron_tagger')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    return


@app.cell
def _(ne_chunk, pos_tag, word_tokenize):
    def nltk_ner(text):
        """
        Extract and categorize named entities from text using NLTK
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

        # Tokenize and tag parts of speech
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)

        # Perform NER
        named_entities = ne_chunk(pos_tags)

        # Extract entities
        for chunk in named_entities:
            if hasattr(chunk, 'label'):
                entity_name = ' '.join(c[0] for c in chunk)
                entity_type = chunk.label()
                if entity_type in entities:
                    entities[entity_type].append(entity_name)

        return entities
    return (nltk_ner,)


@app.cell
def _(nltk_ner):
    # Example usage
    def nltk_extract_ents():
        text = """
        Tim Cook, CEO of Apple Inc., announced yesterday that the company's revenue 
        grew by 15% to reach $365 billion in New York City.
        """
        entities = nltk_ner(text)
        for entity_type, entity_list in entities.items():
            if entity_list:
                print(f"{entity_type}: {entity_list}")

    nltk_extract_ents()
    return (nltk_extract_ents,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## NER using Spacy""")
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
            }
            for ent in doc.ents
        ]

        return entities
    return (spacy_ner,)


@app.cell
def _(spacy_ner):
    def spacy_extract_ents():
        text = """
        Tim Cook, CEO of Apple Inc., announced yesterday that the company's revenue 
        grew by 15% to reach $365 billion in New York City.
        """
        entities = spacy_ner(text)

        for entity in entities:
            print(f"{entity['label']}: {entity['text']}")

    spacy_extract_ents()
    return (spacy_extract_ents,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
