import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")


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


# Example usage
if __name__ == "__main__":
    text = "Microsoft's CEO Satya Nadella visited London last week."
    entities = spacy_ner(text)

    for entity in entities:
        print(f"Entity: {entity['text']}")
        print(f"Type: {entity['label']}")
        print(f"Position: {entity['start']}-{entity['end']}\n")
