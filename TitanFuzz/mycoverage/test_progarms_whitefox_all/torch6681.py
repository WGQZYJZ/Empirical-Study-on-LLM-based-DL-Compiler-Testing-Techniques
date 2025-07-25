import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Sequential(*[torch.nn.ConvTranspose1d(4, 4, 3, stride=1, padding=1)])
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 4, 128)
