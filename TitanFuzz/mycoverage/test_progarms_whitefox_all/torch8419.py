import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(147, 229, kernel_size=(2, 2), stride=(1, 1), padding=(1, 1))
    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = torch.sigmoid(v1)
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 147, 13, 164)
