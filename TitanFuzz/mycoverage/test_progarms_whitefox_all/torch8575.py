import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x = torch.abs(x)
        x = torch.cat([x, x], dim=1)
        x = x.view(int(x.shape[0]), -1)
        x = torch.relu(x)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 3, 4)
