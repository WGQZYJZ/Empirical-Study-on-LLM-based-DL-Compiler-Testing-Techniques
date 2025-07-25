import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(3, 8, kernel_size=(1, 1), stride=(1, 1))
        self.conv_t = torch.nn.ConvTranspose2d(8, 10, kernel_size=(3, 3), stride=(2, 2))
    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = self.conv_t(v1)
        v3 = torch.sigmoid(v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 10, 10)
