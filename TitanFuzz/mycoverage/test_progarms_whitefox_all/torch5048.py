import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(2, 1, (2, 2), stride=(2, 2), padding=(1, 1), output_padding=(0, 0), bias=True)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 5, 10)
