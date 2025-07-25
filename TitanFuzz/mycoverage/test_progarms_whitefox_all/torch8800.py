import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.r = torch.nn.ReLU()
    def forward(self, x1, x2):
        v3 = x1.permute(0, 2, 1)
        return self.r(torch.matmul(v3, x2))
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
