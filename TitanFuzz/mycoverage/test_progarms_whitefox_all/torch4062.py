import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        y = x.view(x.shape[0], -1).tanh()
        x = torch.cat((y, y), dim=1)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2, 2)
