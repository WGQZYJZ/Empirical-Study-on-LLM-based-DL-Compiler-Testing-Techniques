import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * torch.clamp(torch.min(0, torch.max(6, v1 + 3)), min=0, max=6)
        v3 = v2 / 6
        return v3
m = Model()
x1 = torch.randn(1, 2)
