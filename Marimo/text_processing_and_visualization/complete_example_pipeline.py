import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Complete Example Pipeline
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp-workshop](https://www.github.com/a-mhamdi/nlp-workshop)**
        """
    )
    return


@app.cell
def _():
    from LOCAL.advanced_pipeline_with_custom_features import AdvancedTextPreprocessor
    from LOCAL.create_bow import create_bow
    from LOCAL.plot_word_frequency import plot_word_frequency
    from LOCAL.generate_wordcloud import generate_wordcloud
    return (
        AdvancedTextPreprocessor,
        create_bow,
        generate_wordcloud,
        plot_word_frequency,
    )


@app.cell
def _(
    AdvancedTextPreprocessor,
    create_bow,
    generate_wordcloud,
    plot_word_frequency,
):
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
    return (process_and_visualize_text,)


@app.cell
def _(process_and_visualize_text):
    # Example usage
    if __name__ == '__main__':
        sample_text = """
        Natural language processing (NLP) is a subfield of linguistics, computer science, 
        and artificial intelligence concerned with the interactions between computers and 
        human language, in particular how to program computers to process and analyze large 
        amounts of natural language data.
        """

        tokens, bow, features = process_and_visualize_text(sample_text)
    return bow, features, sample_text, tokens


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
