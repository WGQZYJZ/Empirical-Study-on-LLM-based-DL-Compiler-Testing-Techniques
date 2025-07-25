import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
    def forward(self, x1):
        x2 = x1.permute(0, 2, 1)
        y = self.linear.bias
        return torch.nn.functional.relu(y) + x2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
