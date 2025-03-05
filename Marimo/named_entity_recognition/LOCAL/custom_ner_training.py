# Training a Custom Model with spaCy
import spacy
from spacy.tokens import DocBin
from spacy.util import minibatch, compounding


def train_custom_ner(training_data, model=None, output_dir=None, n_iter=100):
    """
    Train a custom NER model

    training_data format:
    [
        ("Text goes here", {"entities": [(0, 4, "LABEL")]}),
        ...
    ]
    """
    if model is not None:
        nlp = spacy.load(model)
    else:
        nlp = spacy.blank("en")

    # Create or get NER component
    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe("ner")
    else:
        ner = nlp.get_pipe("ner")

    # Add labels
    for _, annotations in training_data:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    # Train
    optimizer = nlp.begin_training()
    for itn in range(n_iter):
        losses = {}
        batches = minibatch(training_data, size=compounding(4., 32., 1.001))
        for batch in batches:
            texts, annotations = zip(*batch)
            nlp.update(texts, annotations, drop=0.5, losses=losses)
        print(f"Loss: {losses}")

    # Save model
    if output_dir is not None:
        nlp.to_disk(output_dir)

    return nlp


# Example training data
if __name__ == "__main__":
    training_data = [
        ("Apple Inc. is looking to buy U.K. startup for $1 billion",
         {"entities": [(0, 9, "ORG"), (27, 31, "GPE"), (43, 54, "MONEY")]}),
        ("Microsoft hired new CEO",
         {"entities": [(0, 9, "ORG")]}),
    ]

    # Train model
    custom_model = train_custom_ner(
        training_data, output_dir="custom_ner_model")
