import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value=0.9681, max_value=0.997883):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.sub = torch.sub
        self.min_value = min_value
        self.max_value = max_value
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.sub(self.min_value, self.max_value)
        v3 = torch.clamp(v1, 0.0, v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
