import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 32, (3, 3), (2, 2), padding=1)
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 * 0.75
        return v2
m = Model()
# Inputs to the model
x = torch.randn(1, 16, 64, 64, dtype=torch.float16)
