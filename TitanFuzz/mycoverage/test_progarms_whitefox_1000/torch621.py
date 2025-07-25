import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 1, kernel_size=3, stride=1, padding=1)
        self.softmax = torch.nn.Softmax(dim=0)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tanh(v1)
        v3 = self.softmax(v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 8, 5, 5)
