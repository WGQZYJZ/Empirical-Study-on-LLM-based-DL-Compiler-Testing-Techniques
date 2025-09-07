import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(128, 128)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.softmax(v1)
        v3 = v2 + x
        return v3
m = Model()
# Inputs to the model
x = torch.randn(1, 128)
