import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.features = torch.nn.Sequential(
           torch.nn.Conv2d(3, 16, 1, stride=1, padding=0),
           torch.nn.Conv2d(16, 8, 3, stride=1, padding=0)
        )
    def forward(self, x1):
        v0 = x1
        v1 = self.features(v0)
        v2 = torch.relu(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 256, 256)
