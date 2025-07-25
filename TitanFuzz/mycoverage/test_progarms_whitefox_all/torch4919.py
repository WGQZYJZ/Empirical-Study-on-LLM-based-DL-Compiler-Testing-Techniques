import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 3, 1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(3, 3, 2)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(3, 3, 3, output_padding=1)
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
        v10 = self.conv_transpose2(v9)
        v11 = self.conv_transpose3(v10)
        v12 = v11 * 0.5
        v13 = v11 * v11 * v11
        v14 = v13 * 0.044715
        v15 = v11 + v14
        v16 = v15 * 0.7978845608028654
        v17 = torch.tanh(v16)
        v18 = v17 + 1
        v19 = v12 * v18
        return v19
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 4, 4)
