import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, stride=2)
        self.batch_norm1 = nn.BatchNorm2d(32)
    def forward(self, x):
        return self.conv1(self.batch_norm1(x))
m = Model()
# Inputs to the model       
x = torch.randn(1, 1, 10, 10)
