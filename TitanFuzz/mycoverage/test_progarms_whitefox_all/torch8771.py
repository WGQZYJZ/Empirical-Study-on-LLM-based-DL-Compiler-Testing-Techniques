import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.weight = torch.randn(3, 1)
    def forward(self, x1, x2):
        v1 = torch.mm(x1, self.weight)
        v2 = torch.mm(x2, self.weight)
        return torch.cat((v2, v1, v2), 1)
m = Model()
# Inputs to the model
x1 = torch.randn(2, 3)
x2 = torch.randn(4, 3)
