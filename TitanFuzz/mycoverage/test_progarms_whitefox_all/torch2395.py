import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value=4.7, max_value=0.3):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(5, 5, 1, padding=1)
        self.min_value = min_value
        self.max_value = max_value
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v4 = torch.clamp_max(v2, self.max_value)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 5, 64, 64)
