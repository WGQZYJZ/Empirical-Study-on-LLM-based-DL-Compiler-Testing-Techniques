import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(2, 3, kernel_size=5, stride=2, padding=2, output_padding=1)
        self.conv1 = torch.nn.ConvTranspose2d(3, 1, 1)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = self.conv1(v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 10, 2)
