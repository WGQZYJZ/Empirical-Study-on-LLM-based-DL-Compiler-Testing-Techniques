import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 4, bias=False)
    def forward(self, x):
        x = torch.transpose(x, 0, 1)
        x = self.layers(x)
        x = torch.transpose(x, 0, 1)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
