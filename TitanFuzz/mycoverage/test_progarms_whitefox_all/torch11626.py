import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x1 = torch.cat([x, x], dim=1)
        if len(x.shape) == 1:
            x2 = x1
        else:
            x2 = torch.cat([x1, x1], dim=1)

        x3 = x2.view(x2.shape[0], -1)
        x4 = torch.relu(x3)

        return torch.cat([x3, x4], dim=1)
m = Model()
# Inputs to the model
x = torch.randn(2, 3)
