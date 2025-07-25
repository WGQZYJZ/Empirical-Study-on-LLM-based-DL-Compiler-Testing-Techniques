import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(44, 44, 4, padding=3)
    def forward(self, x):
        x1 = self.conv_t(x)
        x2 = x1 > 0
        x3 = x1 * 0.108
        x4 = torch.where(x2, x1, x3)
        return x4
m = Model()
# Inputs to the model
x = torch.randn(1, 44, 20, 12)
