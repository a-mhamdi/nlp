# NLP Codes Repository


This repository contains `Python` scripts and utilities for **Natural Language Processing** *(NLP)* tasks, primarily using libraries such as `NLTK`, `SpaCy`, and `Gensim`. 

**We use Marimo**, a reactive `Python` notebook for interactive experimentation.

![Marimo Logo](marimo.svg)

## Installation

This project uses `uv` for fast and reliable Python package management. To set up the environment locally:

1. Install `uv` if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Clone the repository and navigate to the directory:
   ```bash
   git clone https://github.com/a-mhamdi/nlp
   cd nlp/codes
   ```

3. Install dependencies using `uv`:
   ```bash
   uv python pin 3.12 # Ensure you have Python 3.12 installed
   uv sync
   ```

This will create a virtual environment and install all required packages as specified in `pyproject.toml`.

4. Run `Marimo` to start the interactive notebook:
   ```bash
   uv run marimo edit
   ```

## Python Files

- **py-onramp.py**: Introductory `Python` code for **NLP** beginners.
- **extracting_named_entities.py**: Notebook for extracting named entities from text.
- **text_processing.py**: General text processing functions.
- **text_visualization.py**: Notebook for visualizing text data _(e.g., word clouds, frequency plots)_.
- **gensim_text_processing.py**: Text processing utilities using the `Gensim` library.