import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self.softmax = torch.nn.Softmax()
    def forward(self, x1):
        v4 = x1
        v1 = torch.nn.functional.linear(v4, self.linear.weight, self.linear.bias)
        a1 = torch.tensor([[1, 2], [3, 4]])
        v2 = v1.permute(0, 2, 1)
        a2 = torch.tensor([[5, 6], [7, 8]])
        v3 = self.softmax(a2)
        return (v1, v2)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2, device='cpu', requires_grad=True)
a3 = torch.tensor(0.0)
