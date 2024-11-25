# Project 3 FYS-STK3155

## Description
NEEDS SOME FORM OF PROJECT DESCRIPTION HERE

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
- `classification_kmeans`: notebook with clustering of data with `KMeans` and `HDBSCAN`using `UMAP`and `PCA`for dimension reduction.
- `classification_neural_net`: notebook with classification of data using a neural net implemented with `PyTorch`.
- `clustering_classification`: 
- `evaluation`: 
- `kmeans_confusion_matrix`:
- `neural_net`: class implementation of neural net using `PyTorch`
- `pca_analysis`: notebook exploring the effects on the accuracy of the neural net when reducing the dimension of the input data with `PCA`.
- `plotting_results`: notebook for plotting many of the figures found in the report using data from the _Results_-folder.
- `preprocessing_sentences`: notebook with processing of texts split into sentences with `nltk`, including embedding with `sentence-transformer`
- `preprocessing`: notebook with all processing of texts, including embedding with `sentence-transformer`.
- `textdataset_classification`: class implementation of dataset for `PyTorch` interface

- **`Data`**:
  - Contains files with datasets for training the classification and clustering models as well as the `torch`-models for classification.
 
- **`Results`**:
  - Accuracy and adjusted rand scores for various runs of classification and clustering.

#### `Generation/`
Contains all files related to implementation of the neural net.
- `generaation`: notebook with implementation of recurrent neural net for generating new text based on previous works

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
