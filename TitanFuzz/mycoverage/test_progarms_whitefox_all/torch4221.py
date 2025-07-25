import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
    def forward(self, x1):
        # A dummy operation on the input tensor
        t1 = x1 + x1 + x1
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        x2 = torch.nn.functional.relu(v2)
        v3 = x2.detach()
        v4 = torch.min(v3, dim=-1)[1]
        x3 = torch.div(x2, v2)
        v5 = x2.detach()
        v6 = torch.max(v5, self.linear.weight)
        z = torch.max(x3, v6)
        return z
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
