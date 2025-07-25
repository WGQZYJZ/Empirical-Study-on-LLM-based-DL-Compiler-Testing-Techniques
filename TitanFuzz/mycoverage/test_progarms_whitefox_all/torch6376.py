import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 5, stride=1, padding=2)
        self.min = min
        self.max = max
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min, out=torch.cuda.FloatTensor())
        v3 = torch.clamp_max(v2, self.max, out=torch.cuda.FloatTensor())
        return v3
m = Model()
min = -0.5
max = 0.2
# Inputs to the model
x1 = torch.randn(1, 3, 32, 256)
