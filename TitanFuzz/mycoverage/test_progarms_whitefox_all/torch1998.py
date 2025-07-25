import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose1 = torch.nn.ConvTranspose2d(3, 64, 3, padding=1, stride=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(64, 64, 3, padding=1, stride=2)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(64, 64, 3, padding=1, stride=1)
        self.conv_transpose4 = torch.nn.ConvTranspose2d(64, 9, 3, padding=1, stride=2)
    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = F.relu(v1)
        v3 = self.conv_transpose2(v2)
        v4 = F.relu(v3)
        v5 = self.conv_transpose3(v4)
        v6 = F.relu(v5)
        v7 = self.conv_transpose4(v6)
        return v7
m = Model()
# Inputs to the model
x1 = torch.randn(4, 3, 128, 128)
