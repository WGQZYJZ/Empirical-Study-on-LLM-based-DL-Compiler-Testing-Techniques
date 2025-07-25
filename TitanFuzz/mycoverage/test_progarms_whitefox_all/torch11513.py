import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.block0 = torch.nn.Sequential(torch.nn.ConvTranspose2d(3, 1, 3, bias=True, padding=0, stride=2), torch.nn.ReLU(inplace=False), torch.nn.Sigmoid())
    def forward(self, x1):
        y = self.block0(x1)
        return y
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
