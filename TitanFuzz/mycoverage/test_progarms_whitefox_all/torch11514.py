import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 32, 1, stride=3, padding=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
