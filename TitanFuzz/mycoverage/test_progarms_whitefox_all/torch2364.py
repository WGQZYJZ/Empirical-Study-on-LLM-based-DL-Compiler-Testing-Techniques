import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose1 = torch.nn.ConvTranspose2d(3, 5, 3, padding=1, stride=2)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(5, 6, 3, padding=1, stride=2)
    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = v1

        v3 = self.conv_transpose2(v2)
        v4 = torch.relu(v3)
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 16, 16)
