#import "Preamble.typ": *

#align(center)[
  #v(0.2em)
  #text(fill: dark, size: 18pt, weight: "bold")[RNN, LSTM & GRU — Time Series Forecasting Lab]
  #v(0.2em)
  #text(fill: teal, size: 10pt, style: "italic")[Predicting Household Energy Consumption · PyTorch · Train from Scratch]
  #v(0.1em)
  #line(length: 100%, stroke: 2pt + teal)
  #v(0.4em)
]

#grid(
  columns: (2fr, 1fr),
  gutter: 10pt,
  [*Students:* #h(1fr) #box(width: 8cm, line(length: 100%, stroke: 0.5pt + border))],
  [*Date:* #h(1fr) #box(width: 3cm, line(length: 100%, stroke: 0.5pt + border))],
)
#v(0.6em)

#block(
  width: 100%, fill: light, radius: 4pt,
  inset: (x: 12pt, y: 8pt),
  stroke: 1pt + border,
)[
  #text(weight: "bold", fill: dark)[Objective: ]
  #text(fill: gray)[
    This lab compares vanilla RNN, LSTM, and GRU on hourly energy forecasting from the UCI Household Power dataset — covering sequence preparation, training, evaluation against a persistence baseline, and hidden-state visualisation to expose what each architecture retains across time. The focus is not on forecasting per se, but on mastering the PyTorch implementation of each recurrent architecture from scratch.
  ]
]

#v(0.5em)

#q("1",
  [Load the dataset (separator `;`, missing values encoded as `?`), combine the `Date` and `Time` columns into a `DatetimeIndex`, resample `Global_active_power` to hourly means, then split and scale — fitting the scaler only on the training set.],
  "Use sep=';' and na_values='?' in read_csv(). Concatenate date+time and pass to pd.to_datetime(). Resample with .resample('h').mean(). Fit StandardScaler on train only to avoid data leakage."
)

#q("2",
  [Write a `create_sequences(series, window, horizon)` function returning tensors `X` of shape `(N, window, 1)` and `y` of shape `(N, horizon)` via a sliding window. Wrap them in a `DataLoader`.],
  "Loop i from 0 to len(series)-window-horizon. X[i]=series[i:i+window], y[i]=series[i+window:i+window+horizon]. Stack with np.stack and convert to torch.FloatTensor."
)

#q("3",
  [Implement a `RecurrentForecaster(nn.Module)` accepting a `cell_type` argument (`'rnn'`, `'lstm'`, `'gru'`). The forward pass returns a prediction from the last time step only. Count trainable parameters for each variant and explain the differences.],
  "Map cell_type to nn.RNN/LSTM/GRU. Unpack LSTM output as (out,(h_n,c_n)). Use output[:,-1,:] through a Linear head. LSTM has ~4× RNN params; GRU ~3×. Use sum(p.numel() for p in model.parameters() if p.requires_grad)."
)

#q("4",
  [Train all three models under identical conditions. Use MSE loss, apply gradient clipping, and implement manual early stopping. Log train and validation loss per epoch.],
  "clip_grad_norm_(model.parameters(), max_norm=1.0) prevents exploding gradients, critical for vanilla RNN. Early stopping: track best val loss; if no improvement after patience epochs, break and restore best state_dict."
)

#q("5",
  [Evaluate on the test set: inverse-transform predictions back to kW, then compute RMSE and MAE per model. Also compute a persistence baseline (next value = current value) and confirm your models beat it.],
  "scaler.inverse_transform() before any metric computation. Persistence RMSE is the minimum bar — if RNN fails to beat it, it has learned nothing about temporal dynamics."
)

#q("6",
  [Plot a 48-hour overlay of ground truth vs. all three predictions. Then extract hidden states, visualise them as a heatmap (time steps × hidden units), and for LSTM plot `h_t` and `c_t` side by side.],
  "RNN activations often saturate near ±1. LSTM: c_t changes slowly (long-term memory), h_t reacts sharply to recent input. Use plt.imshow() or seaborn.heatmap() on the (seq_len, hidden_size) array."
)

#q("7",
  [Summarise results in a table: Model · \#Params · Train Time (s/epoch) · Test RMSE · Test MAE. Then re-train your best model with window sizes 12, 24, 48, 168 h and plot RMSE vs window length.],
  "GRU often matches LSTM accuracy with fewer params and faster training. Energy data has strong 24 h and 168 h cycles — longer windows may help but risk vanishing gradients in vanilla RNN."
)

#v(0.6em)

#line(length: 100%, stroke: 1pt + border)