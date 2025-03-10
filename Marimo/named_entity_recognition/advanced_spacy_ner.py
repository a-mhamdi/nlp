import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Advanced Spacy NER
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
    class NamedEntityExtractor:
        def __init__(self, model="en_core_web_sm"):
            self.nlp = spacy.load(model)

        def analyze_text(self, text):
            """
            Comprehensive NER analysis
            """
            doc = self.nlp(text)

            # Extract entities with context
            analysis = []
            for ent in doc.ents:
                # Get entity context (surrounding words)
                start = max(0, ent.start - 2)
                end = min(len(doc), ent.end + 2)
                context = doc[start:end].text

                analysis.append({
                    'entity': ent.text,
                    'type': ent.label_,
                    'context': context,
                    'explanation': spacy.explain(ent.label_)
                })

            return analysis

        def get_entity_statistics(self, text):
            """
            Generate statistics about entities in text
            """
            doc = self.nlp(text)

            stats = {
                'total_entities': len(doc.ents),
                'entity_types': {},
                'entity_density': len(doc.ents) / len(doc) if len(doc) > 0 else 0
            }

            # Count entity types
            for ent in doc.ents:
                stats['entity_types'][ent.label_] = \
                    stats['entity_types'].get(ent.label_, 0) + 1

            return stats
    return (NamedEntityExtractor,)


@app.cell
def _(NamedEntityExtractor):
    # Example usage
    if __name__ == "__main__":
        extractor = NamedEntityExtractor()

        text = """
        In 2024, Google and Microsoft announced a partnership worth $5 billion. 
        The deal was signed in Seattle by Sundar Pichai and Satya Nadella.
        """

        # Analyze text
        analysis = extractor.analyze_text(text)
        print("Named Entity Analysis:")
        for item in analysis:
            print(f"\nEntity: {item['entity']}")
            print(f"Type: {item['type']} ({item['explanation']})")
            print(f"Context: \"{item['context']}\"")

        # Get statistics
        stats = extractor.get_entity_statistics(text)
        print("\nEntity Statistics:")
        print(f"Total entities found: {stats['total_entities']}")
        print("Entity types distribution:", stats['entity_types'])
        print(f"Entity density: {stats['entity_density']:.2%}")
    return analysis, extractor, item, stats, text


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
