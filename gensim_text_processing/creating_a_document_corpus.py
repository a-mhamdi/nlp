from gensim import corpora

# Sample documents
documents = [
    "The quick brown fox jumps over the lazy dog",
    "Python is a great programming language",
    "Text processing with Gensim is efficient",
    "The lazy dog sleeps all day",
]

# Tokenize documents


def preprocess(text):
    # Convert to lowercase and split into words
    return text.lower().split()


# Process all documents
processed_docs = [preprocess(doc) for doc in documents]

# Create dictionary (maps words to IDs)
dictionary = corpora.Dictionary(processed_docs)

# Convert documents to bag-of-words format
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

print("Dictionary:", dictionary.token2id)
print("\nFirst document BoW:", corpus[0])
