import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.functional.hardtanh
    def forward(self, x165):
        v1 = self.conv(x165, 0.072484244191455, 0.317667305994034, True)
        return v1
m = Model()
# Inputs to the model
x165 = torch.randn(1, 23, 33, 1)
