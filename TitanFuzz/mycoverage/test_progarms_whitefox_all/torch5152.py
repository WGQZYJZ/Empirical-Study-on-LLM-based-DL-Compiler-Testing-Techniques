import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 16, 3, stride=2, padding=1, bias=False)
        self.add = torch.nn.quantized.FloatFunctional()
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.add.add_scalar(v1, 3)
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = torch.div(v4, 6)
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(1, 16, 64, 64)
