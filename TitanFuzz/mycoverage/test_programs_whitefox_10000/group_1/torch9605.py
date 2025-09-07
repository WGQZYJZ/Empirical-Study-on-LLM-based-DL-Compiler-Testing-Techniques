import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.param = torch.randn(3, 3, 3)
    def forward(self, x):
        x = torch.relu(x)
        x = torch.cat([x, torch.tanh(self.param)], dim=-1)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 3, 3)
