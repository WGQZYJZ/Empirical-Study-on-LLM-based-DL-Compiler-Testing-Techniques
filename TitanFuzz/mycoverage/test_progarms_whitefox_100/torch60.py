import torch
from torch import nn
    
class Model(torch.nn.Module):
    def forward(self, x):
        t1 = torch.mm(x, x)
        return torch.mm(x, x) + t1
m = Model()
# Inputs to the model
x = torch.randn(10000, 10000)
