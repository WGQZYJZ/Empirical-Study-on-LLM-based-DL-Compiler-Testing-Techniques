import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(15, 17, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(17, 19, 3, stride=1, padding=1)
    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = 3 + t1
        t3 = torch.clamp(t2, 0, 6)
        t4 = t1 * t3
        t5 = t4 / 6
        t6 = self.conv2(t5)
        return t6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 15, 30, 30)
