import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(3, 9, 1, stride=1, padding=0)
    def forward(self, x4):
        v1 = self.conv_t(x4)
        v2 = v1 > 0
        v3 = v1 * -0.55
        v4 = torch.where(v2, v1, v3)
        return v4
m = Model()
# Inputs to the model
x4 = torch.randn(15, 3, 4, 3)
