import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 5, 50, stride=8, padding=1, output_padding=0, bias=True)
    def forward(self, x5):
        v1 = self.conv_transpose(x5)
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
x5 = torch.randn(7, 8, 4, 32)
