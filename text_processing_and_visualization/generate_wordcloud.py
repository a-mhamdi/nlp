import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    from wordcloud import WordCloud
    from matplotlib import pyplot as plt
    return WordCloud, plt


@app.cell
def _(WordCloud, plt):
    def generate_wordcloud(text):
        wordcloud = WordCloud(
            width=800, height=400,
            background_color='white',
            max_words=100
        ).generate(text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
    return (generate_wordcloud,)


@app.cell
def _():
    if __name__ == '__main__':
        pass
    return


if __name__ == "__main__":
    app.run()
