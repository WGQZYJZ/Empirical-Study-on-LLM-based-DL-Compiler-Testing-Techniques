import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 16, 4, stride=2, padding=2)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 224, 225)
