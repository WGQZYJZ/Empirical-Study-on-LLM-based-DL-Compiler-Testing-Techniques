import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x = torch.cat([x, torch.zeros(x.shape)], dim=0)
        x = torch.relu(x)
        return x
m = Model()
# Inputs to the model
x = torch.randn(3, requires_grad=True)
