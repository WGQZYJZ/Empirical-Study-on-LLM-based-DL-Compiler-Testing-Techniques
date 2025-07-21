import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 3)
    def forward(self, x):
        t1 = torch.addmm(x, self.layers.weight, self.layers.bias)
        x = torch.stack([t1] * 3, dim=1)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
