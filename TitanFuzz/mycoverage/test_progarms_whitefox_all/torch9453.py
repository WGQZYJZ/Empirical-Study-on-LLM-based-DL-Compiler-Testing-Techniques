import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, X, Y):
        y = torch.mm(X, Y)
        x = torch.mm(X, X)
        y = y - x
        return y
m = Model()
# Inputs to the model
X = torch.rand(2, 2)
Y = torch.rand(2, 2)
