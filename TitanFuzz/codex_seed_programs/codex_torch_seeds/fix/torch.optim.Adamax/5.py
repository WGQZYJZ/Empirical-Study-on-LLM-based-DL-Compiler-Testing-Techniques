'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adamax\ntorch.optim.Adamax(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]]
y_data = [[0], [0], [0], [1], [1], [1]]
x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)
print(x_train.shape)
print(y_train.shape)
W = torch.zeros((2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)
optimizer = optim.Adamax([W, b], lr=0.01)
nb_epochs = 1000
for epoch in range((nb_epochs + 1)):
    hypothesis = torch.sigmoid((x_train.matmul(W) + b))