import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
    def forward(self, x1):
        v4 = x1
        v1 = torch.nn.functional.linear(v4, self.linear.weight.to('cuda:1'), self.linear.bias.to('cuda:1'))
        v2 = v1.permute(0, 2, 1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2, device='cuda:0')
