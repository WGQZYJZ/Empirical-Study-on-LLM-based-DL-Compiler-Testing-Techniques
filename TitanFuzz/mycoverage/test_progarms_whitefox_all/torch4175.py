import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose1d(50, 100, kernel_size=(21,), stride=(1,), dilation=(2,), groups=1, bias=False, padding=(49,))
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return v5
m = Model()
# Inputs to the model
x1 = torch.randn(100, 50, 1)
