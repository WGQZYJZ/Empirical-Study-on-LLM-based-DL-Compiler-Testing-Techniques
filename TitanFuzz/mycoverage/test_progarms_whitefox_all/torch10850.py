import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 64)
        self.other = torch.nn.Parameter(torch.randn(64, 64))
 
    def forward(self, x1):
        v1 = self.linear(x1)
        m = Model()
