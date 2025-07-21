import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, X):
        return torch.mm(X, 2)
m = Model()
# Inputs to the model
X = torch.randn(100, 100)
