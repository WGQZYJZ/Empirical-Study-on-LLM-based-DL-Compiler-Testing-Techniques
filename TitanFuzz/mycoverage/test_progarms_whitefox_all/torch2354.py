import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        y = torch.cat((x, x), dim=1).view(x.shape[0], -1)
        x = torch.relu(y)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 3, 4)
