import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu6 = torch.nn.ReLU6()
    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.relu6(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
