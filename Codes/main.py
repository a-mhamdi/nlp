import gensim.downloader as api
import nltk
import os

# Set env vars before importing libraries
os.environ.setdefault("NLTK_DATA", ".venv/share/nltk_data")
os.environ.setdefault("GENSIM_DATA_DIR", ".venv/share/gensim_data")
# export GENSIM_DATA_DIR=".venv/share/gensim_data"

# Create dirs before imports so libraries find them
os.makedirs(".venv/share/nltk_data", exist_ok=True)
os.makedirs(".venv/share/gensim_data", exist_ok=True)


def main():

    # Download NLTK data
    nltk.download(
        [
            'punkt_tab',
            'words',
            'stopwords',
            'averaged_perceptron_tagger_eng',
            'maxent_ne_chunker_tab'
        ],
        download_dir=".venv/share/nltk_data"
    )

    # Cache gensim embeddings locally
    api.load("glove-twitter-25")


if __name__ == "__main__":
    main()
