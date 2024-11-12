# Project 3 FYS-STK3155

## Description
This project aims to find the best fit for simple polynomials and the Franke function using a neural net and various gradient descent methods, as well as classifying benign and malignant tumors from the Wisconsin breast cancer dataset using a neural net and logistic regression.

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
- `neural_net`: class implementation of neural net using `PyTorch`
- `preprocessing`: notebook with all processing of texts, including embedding with `sentence-transformer`

#### `Generation/`
Contains all files related to implementation of the neural net.
- `generaation`: notebook with implementation of recurrent neural net for generating new text based on previous works

- **`Results/`**:
  - Contains printouts from gridsearch and scores for different hyperparameter combinations
 
 #### `Texts/`

## License

The data used in this project is licensed under the Project Gutenberg License - see the [LICENSE]: (License.txt) for details.

## Contributors
- **Jonas Jørgensen Telle**
- **Marius Torsheim**
- **Maria Klüwer Øvrebø**
