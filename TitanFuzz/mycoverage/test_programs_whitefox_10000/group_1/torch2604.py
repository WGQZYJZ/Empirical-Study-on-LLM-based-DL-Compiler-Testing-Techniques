import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 32, kernel_size=1)
    def forward(self, input):
        return self.conv(input) * 1000
m = Model()
# Input to the model
input_dummy = torch.randn(1, 3, 32, 32)
