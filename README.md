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
| Logistic Regression | 0.7079 |
| Random Forest | 0.7747 |
| Multitask NN | 0.7056 |
| Graph NN | 0.7558 |
| AttentiveFP | 0.7416 |

## Results (Per-Task ROC-AUC)

The table below shows ROC-AUC scores for each model across the 12 Tox21 tasks.

| Task | Logistic Regression | Random Forest | Multitask NN | Graph NN |
|------|--------------------|--------------|--------------|----------|
| NR-AR | 0.775 | 0.772 | 0.766 | 0.743 |
| NR-AR-LBD | 0.838 | 0.842 | 0.814 | 0.800 |
| NR-AhR | 0.788 | 0.788 | 0.750 | 0.813 |
| NR-Aromatase | 0.725 | 0.723 | 0.682 | 0.820 |
| NR-ER | 0.633 | 0.638 | 0.591 | 0.716 |
| NR-ER-LBD | 0.764 | 0.795 | 0.687 | 0.817 |
| NR-PPAR-gamma | 0.722 | 0.769 | 0.740 | 0.819 |
| SR-ARE | 0.716 | 0.751 | 0.731 | 0.758 |
| SR-ATAD5 | 0.717 | 0.689 | 0.700 | 0.734 |
| SR-HSE | 0.705 | 0.716 | 0.685 | 0.780 |
| SR-MMP | 0.796 | 0.805 | 0.771 | 0.833 |
| SR-p53 | 0.708 | 0.776 | 0.682 | 0.724 |

## Mean Performance

| Model | Mean ROC-AUC |
|------|-------------|
| Logistic Regression | ~0.78 |
| Random Forest | ~0.77 |
| Multitask NN | ~0.70 |
| Graph NN | ~0.75 |


#### Discussion
The results demonstrate that classical fingerprint-based models, particularly Logistic Regression and Random Forest, achieve strong and consistent performance on the Tox21 dataset. This highlights the effectiveness of molecular fingerprint representations for QSAR modeling, especially in settings with high-dimensional and sparse features.

Hyperparameter tuning of Logistic Regression further shows that stronger regularization improves performance. The best validation ROC-AUC (0.7795) was obtained with ( C = 0.05 ), indicating that controlling model complexity is important for avoiding overfitting in high-dimensional feature spaces.

Graph Neural Networks (GCN) achieve competitive performance while learning directly from molecular graph structures. Although GCN does not outperform classical models overall, it surpasses them on several tasks, including NR-Aromatase, NR-ER, NR-ER-LBD, NR-PPAR-gamma, SR-HSE, and SR-MMP. This suggests that graph-based representations are particularly effective for certain biological endpoints where structural relationships play a key role.

The Multitask Neural Network shows lower performance compared to other models, which may be due to limited training epochs or suboptimal hyperparameter settings. This indicates that fully connected neural networks may require more careful tuning to match the performance of simpler classical approaches.

Per-task analysis reveals substantial variability across toxicity endpoints, indicating that task difficulty is uneven and that different models capture different aspects of molecular information. No single model consistently dominates across all tasks.

Overall, the results suggest that:

- fingerprint-based models remain strong and reliable baselines,

- graph-based models provide task-specific advantages,

- model performance depends on the characteristics of each endpoint.

These findings indicate that combining fingerprint-based and graph-based representations could be a promising direction for improving molecular property prediction in future work.

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
