import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        y = torch.cat((x, x), dim=1).view(x.shape[0], -1)
        z = y.view(y.shape[0], -1)
        return z.add(torch.sin(x)).sigmoid()
m = Model()
# Inputs to the model
x = torch.randn(2, 2, 2)
