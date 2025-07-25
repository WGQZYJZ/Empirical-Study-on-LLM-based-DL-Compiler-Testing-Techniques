import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 12, 1, stride=2, padding=0)
        self.max_pool = torch.nn.MaxPool2d(kernel_size=(1, 4), stride=2, padding=(0, 1))
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.max_pool(v1)
        v3 = v2 - 0.1
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
