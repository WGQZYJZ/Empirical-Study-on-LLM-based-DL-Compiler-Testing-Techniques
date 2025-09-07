import torch
from torch import nn

class ModelTwo(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, A, B, C):
        v1 = torch.mm(A, B)
        v1 = v1 + C
        return v1
m = Model()
# Inputs to the model
A = torch.randn(3, 3)
B = torch.randn(3, 3)
C = torch.randn(3, 3, requires_grad=True)
