import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        y = x.view(x.shape + (1,))
        ret = torch.relu(y)
        return ret
m = Model()
# Inputs to the model
x = torch.randn(100, 100)
