# Molecular Property Prediction with Tox21
#### Overview

This project evaluates several machine learning and deep learning models for molecular toxicity prediction using the Tox21 dataset. The goal is to compare classical QSAR models with neural network approaches for predicting biological activity from molecular structure.

#### Dataset

The Tox21 dataset contains chemical compounds represented as SMILES strings and includes 12 toxicity prediction tasks related to nuclear receptor signaling and stress response pathways.

Each molecule is converted into features using:

ECFP fingerprints for classical machine learning models

molecular graphs for graph neural networks

The dataset is loaded using DeepChem and split into training, validation, and test sets using a scaffold split, which ensures that molecules with different chemical scaffolds appear in different splits.

#### Models Evaluated

The following models were implemented and compared:

Logistic Regression – baseline QSAR model using molecular fingerprints

Random Forest – ensemble learning model for nonlinear feature interactions

Multitask Neural Network – fully connected neural network predicting all tasks simultaneously


#### Evaluation

Model performance was evaluated using ROC-AUC averaged across the 12 tasks in the dataset.

The evaluation pipeline:

1. Train models on the training set


2. Tune or compare models using the validation set


3. Report final performance on the test set

#### Results
| Model | ROC-AUC |
|------|------|
| Logistic Regression | 0.7777 |
| Random Forest | 0.7721 |
| Multitask NN | 0.7043 |
| Graph NN | 0.7502 |

#### Discussion

The results show that classical fingerprint-based models such as Logistic Regression and Random Forest perform strongly on this dataset.

The Graph Neural Network achieves competitive performance while learning directly from molecular graph structure.

The Multitask Neural Network performed slightly worse, which may be due to limited training epochs or model configuration.

Overall, the experiment demonstrates the effectiveness of both classical QSAR approaches and modern deep learning methods for molecular property prediction.

#### Requirements

Key libraries used in this project:

- DeepChem

- scikit-learn

- PyTorch

- DGL

- RDKit

#### Project Goal

This project demonstrates a typical QSAR modeling workflow:


**molecular structure → feature representation → ML model → toxicity prediction**


and compares classical machine learning approaches with graph-based deep learning models.


#### Notes
Graph Neural Network (GCN) – operates directly on molecular graph representations

Classical models use features derived from molecular fingerprints, while graph neural networks learn representations directly from atom and bond structures.
