import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.transposeconv2d0 = torch.nn.ConvTranspose2d(1, 1, stride=2, kernel_size=2, padding=1)
    def forward(self, x1):
        v1 = self.transposeconv2d0(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 3, 6)
