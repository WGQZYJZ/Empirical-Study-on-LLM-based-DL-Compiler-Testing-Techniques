import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.model = torch.nn.Sequential(
            torch.nn.Linear(32,6)
        )
    def forward(self, x):
        v1 = self.model(x)
        return v1 - 0.5
m = Model()
# Inputs to the model
x = torch.randn(10,32)
