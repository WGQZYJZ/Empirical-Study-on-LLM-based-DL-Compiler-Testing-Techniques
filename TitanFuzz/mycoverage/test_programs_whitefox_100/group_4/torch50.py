import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.c = torch.nn.Conv2d(2, 2, 2, bias=False)
        self.bn = torch.nn.BatchNorm2d(2, affine=False)
        self.relu = torch.nn.ReLU(inplace=True)
    def forward(self, x):
        x = self.relu(self.bn(self.c(x)))
        return x
m = Model()
# Inputs to the model
x = torch.randn(1, 2, 2, 2)
