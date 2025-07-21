import torch
from torch import nn

class ModelTanh(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 12, 12, padding=7, groups=3)
        
    def forward(self, x):
        v = self.conv(x)
        return v
m = Model()
# Inputs to the model
tensor = torch.randn(64, 1, 240, 140)
