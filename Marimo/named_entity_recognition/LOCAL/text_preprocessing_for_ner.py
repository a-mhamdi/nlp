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
