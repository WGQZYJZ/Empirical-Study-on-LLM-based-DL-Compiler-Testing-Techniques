import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v2 = x2.permute(0, 2, 1)
        v3 = torch.bmm(x1, v2)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, **ANY NUMBER HERE**)
x2 = torch.randn(1, 2, **ANY NUMBER HERE**)
# Error handling ends

# Model begins
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = x1.permute(1, 2, 0)
        v2 = x2.permute(1, 2, 0)
        v3 = torch.bmm(v1, v2)
        return v3
# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, **ANY NUMBER HERE**)
# Error handling ends
