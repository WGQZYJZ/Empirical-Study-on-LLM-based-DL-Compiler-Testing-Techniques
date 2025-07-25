import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 3, stride=2)
        self.max_pool = torch.nn.MaxPool2d(2, 2, padding=1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = self.max_pool(v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 16, 16)
