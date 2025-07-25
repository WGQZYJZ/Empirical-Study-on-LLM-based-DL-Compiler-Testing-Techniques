import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value=0.0016, max_value=0.0017):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(128, 128, 3, stride=1, padding=0)
        self.min_value = min_value
        self.max_value = max_value
    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 128, 128, 128)
