import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(3, 7, kernel_size=3, stride=5, padding=1)
    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = torch.sigmoid(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(3, 3, 56, 56)
