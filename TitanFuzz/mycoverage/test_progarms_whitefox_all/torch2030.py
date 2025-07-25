import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value=0.4, max_value=1.0):
        super().__init__()
        self.leaky_relu = torch.nn.LeakyReLU()
        self.max_pool2d = torch.nn.MaxPool2d(kernel_size=1, stride=1, padding=0)
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 3, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value
    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.leaky_relu(v3)
        return v4
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 64, 64)
