import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    from gensim import similarities
    from LOCAL.tfidf_with_gensim import create_tfidf_model
    from LOCAL.creating_a_document_corpus import preprocess
    return create_tfidf_model, preprocess, similarities


@app.cell
def _(create_tfidf_model, preprocess, similarities):
    def compute_document_similarity(documents, query):
        """
        Compute similarity between a query and all documents
        """
        # Create TF-IDF model
        dictionary, tfidf_model, corpus_tfidf = create_tfidf_model(documents)

        # Convert query to TF-IDF space
        query_bow = dictionary.doc2bow(preprocess(query))
        query_tfidf = tfidf_model[query_bow]

        # Initialize similarity matrix
        index = similarities.MatrixSimilarity(corpus_tfidf)

        # Compute similarities
        sims = index[query_tfidf]

        # Return sorted similarities
        return list(enumerate(sims))
    return (compute_document_similarity,)


@app.cell
def _(compute_document_similarity):
    # Example usage
    if __name__ == '__main__':
        documents = [
            "The cat sits on the mat",
            "The dog runs in the park",
            "Cats and dogs are pets",
            "The mat is comfortable"
        ]

        query = "Where is the cat sitting?"
        similarities_ = compute_document_similarity(documents, query)

        # Print sorted similarities
        print("\nDocument similarities to query:") 
        for doc_id, score in sorted(similarities_, key=lambda x: x[1], reverse=True):
            print(f"Document {doc_id+1}: {score:.4f} - {documents[doc_id]}")

    return doc_id, documents, query, score, similarities_


if __name__ == "__main__":
    app.run()
