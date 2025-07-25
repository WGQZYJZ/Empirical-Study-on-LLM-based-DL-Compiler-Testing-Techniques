import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = torch.nn.functional.softmax(v2, dim=-1)
        x2 = torch.matmul(v3, v1)
        x2 = x2.permute(0, 2, 1)
        v2 = torch.transpose(v2, -1, -2)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
