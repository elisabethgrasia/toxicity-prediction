# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:14:54 2026

@author: elisa
"""
import deepchem as dc

tasks, datasets, transformers = dc.molnet.load_tox21()
train_dataset, valid_dataset, test_dataset = datasets

print(train_dataset.X.shape)
print(train_dataset.y.shape)



n_tasks = len(tasks)
n_features = train_dataset.X.shape[1]

model = dc.models.MultitaskClassifier(
    n_tasks=n_tasks,
    n_features=n_features,
    layer_sizes=[1000],
    dropouts=0.25,
    learning_rate=0.001
)

model.fit(train_dataset, nb_epoch=10)

metric = dc.metrics.Metric(dc.metrics.roc_auc_score)

train_scores = model.evaluate(train_dataset, [metric], transformers)
valid_scores = model.evaluate(valid_dataset, [metric], transformers)

print("Train:", train_scores)
print("Validation:", valid_scores)

test_scores = model.evaluate(test_dataset, [metric], transformers)
print("Test:", test_scores)

model = dc.models.GraphConvModel(
    n_tasks=len(tasks),
    mode="classification"
)

model = dc.models.MPNNModel(
    n_tasks=len(tasks),
    mode="classification"
)