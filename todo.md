# Project description:

Is it possible to achieve ssimilar/adequate results from cheaper and simpler classification methods as with more expensive methods? KMeans and neural net.

## Recurrent NN: 

- Take sentences from a book and "predict" (generate) new text in the same style. Inspired by Raschka. - implemented, might want to look into structure and randomness - does the randomness of the text affect the results from classification

## Classification  with neural net

- Training input: sentences from the ~5 books (embedded ~50 word chunks), with their class
    - look at the effect of chunk size - does it impact the results?
        - chunk size 50, 100, 150
    - look at the effect of dataset size, how much data do we need to get adequate results?
        - all data, 75%, 50%, (25%) - will have to update after some examination
- Predict input: embedded ~50/150... word chunk (from book or from generated text)
    - Prediction: class of the prediction input.
- Predict on data outside of the training dataset - other books by the authors
- Predict on generated data

## Classification with KMeans/HDBSCAN

- Same setup as above
- Exploration of using UMAP to reduce the dimensions - how little data can we label and still get good results with?

### PCA (Principal Component Analysis)

- How many dimensions do we actually need?


Interesting books:
    Austen (Pride and prejudice)
    Dostoyevsky (Crime and punishment)
    The Bible, Genesis to Deuteronomy (God, King James Bible)
    Cervantes, Don Quixote
    Sturluson (Heimskringla)


### Theory Section

- UMAP
- RNN
- Sentence-transformer - how embeddings work
- PCA?
- Clustering - KMeans/HDBSCAN
