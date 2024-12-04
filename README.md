# Project 3 FYS-STK3155

## Description
The overarching goal of this project is to generate text in the style of famous authors using an RNN, and then to evaluate its performance with classification methods. The project is thus neatly divided into two parts: Generation and discrimination.

### Discrimination
The goal here is to create classification algorithms which accurately attributes a given chunk of text to the correct author. We have chosen five authors in whose style we wish to generate text - Jane Austen, Fyodor Dostoevsky, the authors of the King James Bible (who will be referred to as 'God' throughout the project), Miguel de Cervantes Saavedra, and Snorre Sturluson.

We test FFNNs and clustering methods (KMeans, HDBSCAN) assisted by dimension reduction methods (UMAP, PCA) on both sentences (which of course have varying lengths) and chunks (which are all the same number of words). The classifiers train on data from one work from each author ('Pride and Prejudice', 'Crime and Punishment', 'The King James Bible', 'Don Quixiote', and 'Heimskringla') provided by the Gutenberg project (see LICENSE). 

We want our classifiers to be able to correctly classify other texts by the same authors, which signalizes a stability and means that they are likely well qualified to assess the performance of our generator. Additionally, we are interested in whether one may reduce the amount of labled data without large performance drops, since labeling is perhaps the most expensive part of supervised learning. We do this with our clustering methods, which make use of a subset of the labels to assist the otherwise unsupervised learning.

### Generation
We use a RNN to generate text in the style of our five chosen authors, testing different temperatures.
<!---
(Here is a sample text from BOOK:) 
-->

## Project Structure
The project is organized into several directories.

### `Report/`
Contains the report written for this project in pdf-format.

#### `Report Title`
The report in pdf format

- **`Figures/`**
  - Contains all figures used in the report.

- **`Additional_plots/`**
  - Contains all additonal figures and plots not included in the report.

### `Code/`
Contains all code used in the project

#### `Classification/`
Class implementation of all gradient descent methods, as well as implementation of class with figures.
- `classification_kmeans`: notebook with clustering of data with `KMeans` and `HDBSCAN` using `UMAP` and `PCA` for dimension reduction.
- `classification_neural_net`: notebook with classification of data using a neural net implemented with `PyTorch`.
- `clustering_classification`: notebook to evaluate the performance and generate design matrices for the clustering methods obtained in `classification_kmeans`.
- `evaluation`: notebook to evaluate the performance of our RNN text generator, using the best neural net classifier.
- `kmeans_confusion_matrix`: notebook exploring the effect of the proportion of labeled training data in the `UMAP` reduction on the train dataset performance of `KMeans` and `HDBSCAN`.
- `neural_net`: class implementation of neural net using `PyTorch`.
- `pca_analysis`: notebook exploring the effects on the accuracy of the neural net when reducing the dimension of the input data with `PCA`.
- `plotting_results`: notebook for plotting many of the figures found in the report using data from the _Results_-folder.
- `preprocessing_sentences`: notebook with processing of texts split into sentences with `nltk`, including embedding with `sentence-transformer`
- `preprocessing`: notebook with all processing of texts, including embedding with `sentence-transformer`.
- `textdataset_classification`: class implementation of dataset for `PyTorch` interface.

- **`Data`**:
  - Contains files with datasets for training the classification and clustering models as well as the `torch`-models for classification.
 
- **`Results`**:
  - Accuracy and adjusted rand scores for various runs of classification and clustering.

#### `Generation/`
Contains all files related to implementation of the neural net.
- `generation`: notebook with implementation of recurrent neural net for generating new text based on previous works.
- `rnn`: class implementation of recurrent neural net.
- `textdataset_generation`: class implementation of dataset for `PyTorch` interface

- **`Models_and_Data`**:
  - Contains saved `torch`-models, a `.txt`-file of the most common English words and the embeddings of the generated text as `.npy`-files.
 
 #### `Texts/`
 Contains all texts in `.txt` format from Project Gutenberg, as well as the embeddings of each text for different embedding sizes saved as `.npy`-files.

## License

The data used in this project is licensed under the Project Gutenberg License - see the [LICENSE](LICENSE) for details.

## Contributors
- **Jonas Jørgensen Telle**
- **Marius Torsheim**
- **Maria Klüwer Øvrebø**
