import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(32, 3, 1, padding=1, stride=2)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = v2.transpose(2, 3).transpose(1, 2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 32, 224, 224)
