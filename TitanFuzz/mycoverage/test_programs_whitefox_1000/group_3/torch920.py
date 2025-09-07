import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1, 3)
        v2 = x2.permute(0, 2, 1, 3)
        v3 = torch.nn.functional.conv2d(v1, v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2, 2)
x2 = torch.randn(1, 2, 2, 2)
