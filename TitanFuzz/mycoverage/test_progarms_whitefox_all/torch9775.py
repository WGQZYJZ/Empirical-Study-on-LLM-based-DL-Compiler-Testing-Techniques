import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        return torch.matmul(x1, x1.permute(0, 1, 2))
m = Model()
# Inputs to the model
x1 = torch.randn(2, 2, 2)
