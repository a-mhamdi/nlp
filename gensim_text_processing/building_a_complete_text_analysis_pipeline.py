import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    from gensim import corpora, models, similarities
    from LOCAL.creating_a_document_corpus import preprocess
    return corpora, models, preprocess, similarities


@app.cell
def _(corpora, models, preprocess, similarities):
    class GensimTextAnalyzer:
        def __init__(self):
            self.dictionary = None
            self.tfidf_model = None
            self.similarity_index = None

        def fit(self, documents):
            """Train the analyzer on a corpus of documents"""
            # Preprocess documents
            processed_docs = [preprocess(doc) for doc in documents]

            # Create dictionary
            self.dictionary = corpora.Dictionary(processed_docs)

            # Create BOW corpus
            bow_corpus = [self.dictionary.doc2bow(doc) for doc in processed_docs]

            # Create TF-IDF model
            self.tfidf_model = models.TfidfModel(bow_corpus)

            # Transform corpus to TF-IDF space
            corpus_tfidf = self.tfidf_model[bow_corpus]

            # Create similarity index
            self.similarity_index = similarities.MatrixSimilarity(corpus_tfidf)

        def get_similar_documents(self, query, top_n=5):
            """Find most similar documents to query"""
            # Process query
            query_bow = self.dictionary.doc2bow(preprocess(query))
            query_tfidf = self.tfidf_model[query_bow]

            # Compute similarities
            sims = self.similarity_index[query_tfidf]

            # Return top N similar documents
            return sorted(enumerate(sims), key=lambda x: x[1], reverse=True)[:top_n]
    return (GensimTextAnalyzer,)


@app.cell
def _(GensimTextAnalyzer):
    # Example usage
    if __name__ == '__main__':
        analyzer = GensimTextAnalyzer()

        documents = [
            "Artificial intelligence is transforming industries",
            "Machine learning models need good data",
            "Deep learning requires powerful GPUs",
            "Data science combines statistics and programming",
            "Neural networks are inspired by biology"
        ]

        # Train analyzer
        analyzer.fit(documents)

        # Find similar documents
        query = "How is AI changing the world?"
        similar_docs = analyzer.get_similar_documents(query)

        print("\nMost similar documents to query:")
        for doc_id, score in similar_docs:
            print(f"Score: {score:.4f} - {documents[doc_id]}")
    return analyzer, doc_id, documents, query, score, similar_docs


if __name__ == "__main__":
    app.run()
