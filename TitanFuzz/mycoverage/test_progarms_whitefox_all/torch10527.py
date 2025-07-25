import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        y = x * 2
        x = torch.cat((y, y, y, y), dim=None)
        return x.view(x.shape[0], -1).tanh()
m = Model()
# Inputs to the model
x = torch.randn(5, 3, 4)
