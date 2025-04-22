# Predicting-Bends-in-Transmembrane-helices.
Aims to develop a Machine learning model that will predict bends or kink in Transmembrane helices.

This repository is still being completed. Here is the summary of the project. The
codes and the related files are being uploaded.

You can jump to the Analysis and the Model subheading if you want to skip the theory.

We have a limited dataset of experimentally determined protein structures. These are
obtained through various methods including X-ray crystallography.

## Theory
The plasma membrane of a cell contains secondary protein structures called Transmembrane helices, which
are responsible for various functions inside the cell including transporting, recepting, etc.
These structures form helices due to intra-helical hydrogen bonds. This bond is
formed between i(th) residue and i+4(th) residue of the helix. Often times there are bends or kinks
in these helices due to various reasons. These bends are necessary for the cells to do their proper functioning.

## Methodology
Data for all the transmembrane proteins was downloaded from : https://www.blanco.biomol.uci.edu/mpstruc/
A total of 2781 proteins were downloaded. Now the aim was to train the model with the helices that were bend.

# Analysis
1. All the helices present in the proteins were analysed if they have a bend or not.
   This was done by checking if the distance between specific atoms of the i(th) and i+4th residue was longer
   than a certain threshold. ( Specific atoms being O of carbonyl and backbone N of ith and i+4th residue respectively.

2. After obtaining all the helices that were bend, it was time to find the angle of bend. This was done using
   vector operation. The vector of the helical axis before the bend and after the bend was calculated. Then, using the
   dot-product the angle between these two vectors were obtained.

3. Now the task was to develop a machine learning model that takes the data of bend helices along with straight helices
   and predicts a random helical sequence having a bend or not.

## The ML Model
1.  Neural Network
   The thought is to develop a neural network (NN) that will simply take in the residues of the helices along with a      label  showing whether it is bend or not. So a NN model was developed with an input layer containing 50 neurons. 
   This will be taking in the residues of the helices.

# Model Architecture

Input Layer
Shape: (50,)
Each sample is a fixed-length amino acid sequence of 50 residues. The amino acids are represented by integer values from 0 to 20 (20 amino acids + a padding/absence token 0).

Embedding Layer
Purpose: Converts integer-encoded amino acids into dense vector representations that can be learned during training.

Parameters:
input_dim=21 (vocabulary size)
output_dim=20 (embedding dimension)

This allows the model to capture similarities between amino acids beyond their numerical label.

Flatten Layer
The 2D embedded output is flattened into a single 1D vector, making it compatible for input to the dense layers.

Hidden Layers
Dense Layer 1
Dense(128, activation='relu')
Followed by:
BatchNormalization()
Normalizes activations to improve training stability and speed.

Dropout(0.3)
Randomly drops 30% of neurons during training to prevent overfitting.

Dense Layer 2
Dense(64, activation='relu')
Followed by:
BatchNormalization()

Dropout(0.3)

Dense Layer 3
Dense(32, activation='relu')
Provides another level of feature abstraction before final prediction.

Output Layer
Output
Dense(1, activation='sigmoid')

Outputs a single probability value between 0 and 1.

sigmoid is ideal for binary classification tasks like bend prediction.

Optimization Details
Loss Function:
binary_crossentropy
Used for binary classification problems to measure the difference between the predicted probabilities and the actual class labels.

Optimizer:
Adam optimizer

Learning rate: 0.001
Adam combines the benefits of momentum and adaptive learning rates, making it highly effective for deep learning tasks.

This was giving a descent Training accuracy around 80 percent.
But when this model was tested against the structures determined by alpha fold model, it performed poorly.
So as of now, My Professor has instructor me to use Support vector machine to do the classification.
