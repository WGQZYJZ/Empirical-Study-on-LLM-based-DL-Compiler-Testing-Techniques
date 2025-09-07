import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x = F.dropout(x, p=torch.nn.functional.relu(torch.randn(())).item())
        x = torch.rand(())
        return x
m = Model()
# Inputs to the model
x = torch.randn(1, 1, 2)
