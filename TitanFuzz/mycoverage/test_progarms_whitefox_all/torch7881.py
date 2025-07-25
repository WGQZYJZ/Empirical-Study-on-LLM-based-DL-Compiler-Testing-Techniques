import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = torch.max(v2, dim=-1)[0]
        v4 = v3.unsqueeze(dim=-1)
        v5 = v4.to(v3.dtype)
        v6 = (v5 == -1).to(v3.dtype)
        v4 = v5 + v6
        v5 = v2 + v4
        v4 = torch.max(v5, -1)[0]
        return v4
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
