import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose_1_3 = torch.nn.ConvTranspose2d(64, 64, 1, stride=2, padding=0, output_padding=2)
    def forward(self, x1):
        v1 = self.conv_transpose_1_3(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 64, 20, 17)
