import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 32, 3, stride=2, padding=0)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 123, 123)
