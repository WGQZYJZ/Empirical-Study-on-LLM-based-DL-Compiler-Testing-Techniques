import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min, max, kernel_size):
        super().__init__()
        self.conv = torch.nn.Conv1d(1, 3, kernel_size)
        self.min = min
        self.max = max
    def forward(self, input):
        v1 = self.conv(input)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        return v3
m = Model()
# Inputs to the model
input = torch.randn(2, 1, 64)
