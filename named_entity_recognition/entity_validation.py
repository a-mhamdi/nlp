import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


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


if __name__ == "__main__":
    app.run()
