import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, input_tensor):
        x1 = x2 * x3
        return x1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
