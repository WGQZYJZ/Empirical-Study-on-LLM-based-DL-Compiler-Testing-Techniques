import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t_r = torch.nn.ConvTranspose2d(64, 1, 3, stride=1, padding=1, output_padding=1)
    def forward(self, x1):
        v1 = self.conv_t_r(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 64, 32, 32)
