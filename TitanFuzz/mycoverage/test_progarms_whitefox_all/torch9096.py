import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose_5 = torch.nn.ConvTranspose2d(23, 23, 3, stride=2, padding=0, output_padding=1)
    def forward(self, x1):
        v1 = self.conv_transpose_5(x1)
        v2 = torch.nn.Sigmoid()(v1)
        v3 = v1 * v2
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 8, 63, 63)
