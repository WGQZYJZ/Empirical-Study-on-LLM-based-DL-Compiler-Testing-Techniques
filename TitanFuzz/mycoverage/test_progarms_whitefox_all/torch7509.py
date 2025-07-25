import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose1 = torch.nn.Conv2d(1, 128, 3, stride=1, padding=1)
    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
