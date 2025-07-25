import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.avg_pool = torch.nn.AvgPool2d(2, 2)
        self.conv_transpose = torch.nn.ConvTranspose2d(32, 15, 3, stride=1, padding=1, output_padding=0)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = torch.relu(v2)
        v4 = torch.clamp(v3, min=0)
        v5 = v1 * v4
        v6 = v5 / 6
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 32, 36, 36)
