import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.gelu = torch.nn.functional.gelu
    def forward(self, input):
        x2 = input.double()
        x3 = self.gelu(x2)
        return x3
m = Model()
# Inputs to the model
input = torch.randn(1, 8, 8)
