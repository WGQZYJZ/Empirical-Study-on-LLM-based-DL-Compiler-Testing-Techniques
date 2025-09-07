import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, y):
        t1 = torch.mm(y, y)
        t2 = torch.mm(y, y)
        out = t1 + t2 + t1
        return t2 + out
m = Model()
# Input to the model
y = torch.randn(100, 100)
