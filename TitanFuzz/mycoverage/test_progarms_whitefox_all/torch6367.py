import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 13, kernel_size=(2, 1))
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 - 123
        v3 = F.relu(v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 16, 16)
