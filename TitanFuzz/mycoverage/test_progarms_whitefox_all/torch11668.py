import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value=50., max_value=150.):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(20, 10, 3, padding=1)
        self.min_value = min_value
        self.max_value = max_value
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(8, 20, 2, 2)
