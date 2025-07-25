import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv_other = other
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.conv_other # Add the other tensor
        return v2

m = Model()
# Initializing the model
m = Model(torch.randn(8, 3, 8, 8))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
