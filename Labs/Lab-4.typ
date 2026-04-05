#import "Preamble.typ": *

#align(center)[
  #v(0.2em)
  #text(fill: dark, size: 18pt, weight: "bold")[Transformers for Question Answering]
  #v(0.2em)
  #text(fill: teal, size: 10pt, style: "italic")[Extractive QA with HuggingFace Transformers · Fine-tuning BERT on SQuAD]
  #v(0.1em)
  #line(length: 100%, stroke: 2pt + teal)
  #v(0.4em)
]

#grid(columns: (2fr, 1fr), 
  gutter: 10pt,
  [*Students:* #h(1fr) #box(width: 8cm, line(length: 100%, stroke: 0.5pt + border))],
  [*Date:* #h(1fr) #box(width: 3cm, line(length: 100%, stroke: 0.5pt + border))],
)
#v(0.6em)

#block(width: 100%, fill: light, radius: 4pt, inset: (x: 12pt, y: 8pt), stroke: 1pt + border)[
  #text(weight: "bold", fill: dark)[Objective: ]
  #text(fill: gray)[This lab introduces extractive QA with BERT on SQuAD v1.1 — tokenising passage-question pairs, running inference with a pretrained QA pipeline, and inspecting attention patterns to see how the model locates answer spans.]
]

#v(0.5em)

#q("1",
  [In extractive QA, the model predicts two integers over the tokenised `[CLS] question [SEP] context [SEP]` input. What do they represent, and how do you recover the answer string from them?],
  "The two integers are start and end token indices. The answer is tokens[start : end+1] extracted from the context. The [CLS] token is used as the unanswerable fallback — point both indices there if no valid span exists in the chunk."
)

#q("2",
  [Load the SQuAD dataset with `load_dataset('rajpurkar/squad')` and inspect one example. Tokenise it with `AutoTokenizer` using `max_length=384` and `stride=128`. Why are these two parameters necessary?],
  "BERT's hard limit is 512 tokens. max_length=384 caps each chunk; stride=128 creates overlapping chunks so an answer near a boundary is not silently cut off. Use truncation='only_second' to truncate the context, never the question."
)

#q("3", // model='bert-large-uncased-whole-word-masking-finetuned-squad'
  [Load `AutoModelForQuestionAnswering.from_pretrained('bert-base-uncased')` and describe what it adds on top of the base BERT. Run a forward pass on your tokenised example and inspect the shape of `start_logits` and `end_logits`.],
  "The QA head is a single Linear(hidden_size, 2) projecting each token representation to two scores. Output shape is (seq_len,) for each. The best span maximises start_logits[i] + end_logits[j] subject to i ≤ j."
)

#q("4",
  [Use the `pipeline('question-answering')` shortcut to run inference on three examples from the validation set — no training required. Print the predicted answer, score, and ground-truth for each.],
  "from transformers import pipeline; qa = pipeline('question-answering', model='bert-base-uncased'). Pass a dict with keys question and context. Compare qa(...)['answer'] against example['answers']['text'][0]."
)

#q("5",
  [Compute Exact Match and F1 on your three examples manually. Then retrieve the attention weights (`output_attentions=True`) and plot a heatmap of one head in the last layer between question tokens (rows) and context tokens (columns).],
  "EM=1 only on exact string match after lowercasing and stripping punctuation. F1 measures token overlap. For the heatmap, use attentions[-1][0, head_idx] sliced to (n_question_tokens, n_context_tokens) — bright columns should cluster around the answer span."
)

#v(0.5em)

#line(length: 100%, stroke: 1pt + border)