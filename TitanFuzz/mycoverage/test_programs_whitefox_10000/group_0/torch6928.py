import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = Conv3D(1, 16, (4, 3, 3))
        self.norm = BatchNorm3d(16, track_running_stats=1)
    def forward(self, x):
        x = self.conv(x)
        x = self.norm(x)
        return x
m = Model()
# Inputs to the model
x = torch.randn(1, 1, 8, 64, 128)
