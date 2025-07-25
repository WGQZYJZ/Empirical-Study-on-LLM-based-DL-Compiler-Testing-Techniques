import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 2, 1)
        return v2.index_select(dim=1, index=torch.tensor([1, 0, 1]))
m = Model()
# Inputs to the model
x1 = torch.randn(2, 2, 2)
