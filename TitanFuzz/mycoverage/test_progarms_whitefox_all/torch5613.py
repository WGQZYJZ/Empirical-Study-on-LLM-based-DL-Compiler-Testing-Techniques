import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t1 = torch.nn.ConvTranspose2d(3, 2, 2, padding=1, stride=2)
        self.conv_t2 = torch.nn.ConvTranspose2d(2, 1, 2, padding=1, stride=2)
    def forward(self, x1):
        v1 = self.conv_t1(x1)
        v2 = self.conv_t2(v1)
        v3 = torch.sigmoid(v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 4, 4)
