import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 128)
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = torch.cat((x1, v1), dim=1)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(2, 128)
