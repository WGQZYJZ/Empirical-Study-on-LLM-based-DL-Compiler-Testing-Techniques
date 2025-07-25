import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 3, (1, 3), stride=(1, 1), padding=(0, 1))
        self.conv2 = torch.nn.Conv2d(3, 3, (1, 1), stride=(1, 1), padding=(0, 0))
    def forward(self, x1):
        v1 = torch.sigmoid(self.conv1(x1))
        v2 = torch.sigmoid(self.conv2(v1))
        return v2
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 28, 28)
