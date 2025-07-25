import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose1 = torch.nn.ConvTranspose2d(13, 6, padding=1, kernel_size=3, stride=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(88, 3, kernel_size=(4, 2), stride=1, padding=0)
    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v1 * v4
        v6 = v5 / 6
        v7 = self.conv_transpose2(v6)
        v8 = v7 - 5
        v9 = torch.clamp(v8, min=-3)
        return F.dropout(v9)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 13, 8, 2)
