from sklearn.feature_extraction.text import TfidfVectorizer


def create_tfidf(documents):
    # Initialize TF-IDF vectorizer
    tfidf = TfidfVectorizer()
    # Create TF-IDF matrix
    X = tfidf.fit_transform(documents)
    # Get feature names
    feature_names = tfidf.get_feature_names_out()

    return X.toarray(), feature_names, tfidf


if __name__ == '__main__':
    pass
