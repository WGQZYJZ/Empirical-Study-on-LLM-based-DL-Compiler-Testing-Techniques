import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.cat = torch.cat
        self.transpose = torch.transpose
    def forward(self, x):
        x = self.cat([x] * 4, dim=1)
        x = self.transpose(x, -1, -2)
        return x
m = Model()
# Inputs to the model
x = torch.randn(3, 3, 3, 6)
