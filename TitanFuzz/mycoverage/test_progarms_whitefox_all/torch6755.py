import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 3, 3, stride=2, padding=1)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.relu(v1)
        v3 = torch.tanh(v2)
        v4 = torch.abs(v3)
        v5 = v4
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 16, 16)
