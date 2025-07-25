import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 1, (1, 1), stride=(1, 1))
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        v10 = v9.squeeze(dim=-1)
        v11 = v10.squeeze(dim=-1)
        v12 = v11.squeeze(dim=0)
        return v12
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 1, 1)
