import torch
from torch import nn

class model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        b1 = torch.nn.functional.dropout(x, p=0.3)
        b2 = torch.nn.functional.dropout(x, p=0.3)
        return 1
# Inputs to the model
x = torch.randn(1)
