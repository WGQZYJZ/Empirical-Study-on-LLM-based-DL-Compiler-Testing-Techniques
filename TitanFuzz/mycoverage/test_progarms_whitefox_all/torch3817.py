import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        y = torch.cat((x, x, x), dim=1)
        x = y.view(x.shape[0], -1).tanh()
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 3, 4)
