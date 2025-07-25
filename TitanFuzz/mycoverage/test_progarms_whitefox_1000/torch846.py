import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.Sequential(
            torch.nn.ConvTranspose2d(4, 8, 3, stride=2, output_padding=1),
            torch.nn.Softplus()
        )
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tanh(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 4, 136, 44)
