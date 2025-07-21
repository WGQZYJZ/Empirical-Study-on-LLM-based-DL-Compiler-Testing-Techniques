import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x):
        t1 = torch.mm(x, x)
        t1 = t1 + torch.mm(x, x)
        t1 = t1 + torch.mm(x, x)
        t1 = t1 + torch.mm(x, x)
        t1 = t1 + torch.mm(x, x)
        t1 = t1 + torch.mm(x, x)
        t1 = t1 + torch.mm(x, x)
        t1 = t1 + torch.mm(x, x)
        t1 = t1 + torch.mm(x, x)
        t1 = t1 + torch.mm(x, x)
        return t1
m = Model()
# Inputs to the model
X = torch.rand(1, 6)
