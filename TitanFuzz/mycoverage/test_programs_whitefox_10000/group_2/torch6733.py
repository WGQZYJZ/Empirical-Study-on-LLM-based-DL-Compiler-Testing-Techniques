import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, A, B):
        t = torch.mm(A, A)
        return torch.mm(B, torch.mm(t, torch.mm(A, B)))
m = Model()
# Inputs to the model
A = torch.randn(100, 100)
B = torch.randn(100, 100)
