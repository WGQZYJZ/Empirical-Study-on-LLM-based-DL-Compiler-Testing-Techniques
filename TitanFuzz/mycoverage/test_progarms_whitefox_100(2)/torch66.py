import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(21, 8, (2, 2), stride=1, padding=(1, 1))
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tanh(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 21, 7, 6)
