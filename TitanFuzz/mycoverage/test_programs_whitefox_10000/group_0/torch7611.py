import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        y = torch.relu(x1)
        return y
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 320, 320)
