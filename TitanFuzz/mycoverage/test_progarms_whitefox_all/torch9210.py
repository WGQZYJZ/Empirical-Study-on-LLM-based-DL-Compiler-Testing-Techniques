import torch
from torch import nn

class Model(nn.Module):
    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12):
        h1 = torch.mm(x1, x2)
        h2 = torch.mm(x2, x3)
        h3 = torch.mm(x3, x4)
        h4 = torch.mm(x4, x5)
        h5 = torch.mm(x5, x6)
        h6 = torch.mm(x6, x7)
        h7 = torch.mm(x7, x8)
        h8 = torch.mm(x8, x9)
        h9 = torch.mm(x9, x10)
        h10 = torch.mm(x10, x11)
        h11 = torch.mm(x11, x12)
        h12 = torch.mm(x12, x13)
        h13 = torch.mm(x13, x14)
        return h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8 + h9 + h10 + h11 + h12 + h13
m = Model()
# Inputs to the model
x1 = torch.randn(4, 4)
x2 = torch.randn(4, 4)
x3 = torch.randn(4, 4)
x4 = torch.randn(4, 4)
x5 = torch.randn(4, 4)
x6 = torch.randn(4, 4)
x7 = torch.randn(4, 4)
x8 = torch.randn(4, 4)
x9 = torch.randn(4, 4)
x10 = torch.randn(4, 4)
x11 = torch.randn(4, 4)
x12 = torch.randn(4, 4)
x13 = torch.randn(4, 4)
x14 = torch.randn(4, 4)
