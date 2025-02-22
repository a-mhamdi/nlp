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
