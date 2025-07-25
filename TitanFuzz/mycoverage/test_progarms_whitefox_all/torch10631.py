import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose1d(2, 1, 2)
    def forward(self, x2):
        x1 = self.conv_t(x2)
        x2 = x1 > 0
        x3 = x1 * 0.12
        x4 = torch.where(x2, x1, x3)
        return x4
m = Model()
# Inputs to the model
x2 = torch.randn(1, 2, 44)
