import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x1, x2)
        return torch.cat([v2, v2, v2], 1)
m = Model()
# Inputs to the model
x1 = torch.randn(128, 512)
x2 = torch.randn(512, 128)
