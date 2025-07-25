import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.tconv2d = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
    def forward(self, x1):
        v1 = self.tconv2d(x1)
        v2 = torch.sigmoid(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
