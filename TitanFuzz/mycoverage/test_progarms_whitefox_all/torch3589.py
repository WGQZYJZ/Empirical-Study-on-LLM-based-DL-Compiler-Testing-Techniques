import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    def forward(self, x1, other=0, groups=3):
        v1 = self.conv(x1)
        if groups == 3:
            groups = torch.randn(v1.shape).long()
            # groups = torch.empty(v1.shape).random_(size=v1.shape).long()
        v2 = v1 + other
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(3, 3, 64, 64)
