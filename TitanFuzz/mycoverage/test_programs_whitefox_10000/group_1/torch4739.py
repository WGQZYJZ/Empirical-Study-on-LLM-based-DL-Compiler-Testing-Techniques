import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x = torch.add(x, x)
        print(x.view(-1).shape)
        x = x.view(-1).relu()
        x = x.view(*x.shape)
        return x
m = Model()
# Inputs to the model
x = torch.ones(4, 4)
