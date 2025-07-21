import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        return torch.cat([torch.mm(x1, x2), torch.nn.functional.dropout(torch.mm(x1, x2), 0.5), torch.nn.functional.relu(torch.mm(x1, x2)), torch.nn.functional.celu(torch.mm(x1, x2))])
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2)
x2 = torch.randn(2, 1)
