from basic_ner_with_nltk import nltk_ner


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
