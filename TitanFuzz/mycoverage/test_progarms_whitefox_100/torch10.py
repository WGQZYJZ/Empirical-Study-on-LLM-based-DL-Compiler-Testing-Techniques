import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        x11 = torch.transpose(x1, 0, 1)
        torch.squeeze(x11, 1)
        v2 = torch.mm(x11, v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(3, 3, requires_grad=True)
x2 = torch.randn(3, 3)
