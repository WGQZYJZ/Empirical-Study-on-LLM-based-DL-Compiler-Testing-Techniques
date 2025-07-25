import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.matmul(v1, x2.permute(0, 2, 1))
        x = torch.matmul(x1.permute(0, 2, 1), v2)
        out1 = x
        out2 = x
        out3 = x
        return (out1, out2, out3)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 1)
x2 = torch.randn(1, 1, 1)
