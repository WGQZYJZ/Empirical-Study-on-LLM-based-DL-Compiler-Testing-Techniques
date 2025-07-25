import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(1000, 550, kernel_size=5, stride=4, padding=0)
    def forward(self, x1):
        v1 = self.conv_t(x1)
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1000, 6, 6)
