from advanced_pipeline_with_custom_features import AdvancedTextPreprocessor
from create_bow import create_bow
from plot_word_frequency import plot_word_frequency
from generate_wordcloud import generate_wordcloud


def process_and_visualize_text(text):
    # Initialize preprocessor
    preprocessor = AdvancedTextPreprocessor()

    # Process text
    tokens = preprocessor.process(text)

    # Create BOW representation
    bow_array, features, _ = create_bow([' '.join(tokens)])

    # Create visualizations
    print("Processed tokens:", tokens)
    print("\nBag of Words representation:")
    print("Features:", features)
    print("BOW array:", bow_array)

    # Generate word frequency plot
    plot_word_frequency(' '.join(tokens))

    # Generate word cloud
    generate_wordcloud(' '.join(tokens))

    return tokens, bow_array, features


# Example usage
if __name__ == '__main__':
    sample_text = """
    Natural language processing (NLP) is a subfield of linguistics, computer science, 
    and artificial intelligence concerned with the interactions between computers and 
    human language, in particular how to program computers to process and analyze large 
    amounts of natural language data.
    """

    tokens, bow, features = process_and_visualize_text(sample_text)
