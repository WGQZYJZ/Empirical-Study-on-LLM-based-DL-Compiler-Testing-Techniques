import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.addmm = torch.addmm
    def forward(self, x):
        x = self.addmm(x, torch.rand(2, 2), torch.rand(2, 2))
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
