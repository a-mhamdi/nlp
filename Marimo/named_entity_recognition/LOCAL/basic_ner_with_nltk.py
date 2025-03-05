import nltk
from nltk import ne_chunk
from nltk import word_tokenize, pos_tag

# Download required NLTK data
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def nltk_ner(text):
    # Tokenize and tag parts of speech
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)

    # Perform NER
    named_entities = ne_chunk(pos_tags)

    return named_entities


# Example usage
if __name__ == "__main__":
    text = "John works at Google in New York."
    entities = nltk_ner(text)
    print(entities)
