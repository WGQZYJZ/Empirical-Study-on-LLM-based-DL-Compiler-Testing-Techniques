import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(16, 3, 5, stride=2, padding=0, output_padding=1, groups=1, bias=True, dilation=1)
    def forward(self, x1):
        v1 = self.deconv(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        return v9
m = Model()
# Inputs to the model
x1 = torch.randn(2, 16, 8, 5)
