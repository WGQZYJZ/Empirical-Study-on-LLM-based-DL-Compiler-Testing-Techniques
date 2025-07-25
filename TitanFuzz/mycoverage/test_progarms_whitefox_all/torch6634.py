import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.depthwise_conv_transpose = torch.nn.ConvTranspose2d(32, 32, 3, groups=32)
    def forward(self, x1):
        v1 = self.depthwise_conv_transpose(x1)
        v2 = torch.relu(v1)
        v3 = torch.sigmoid(v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 32, 16, 16)
