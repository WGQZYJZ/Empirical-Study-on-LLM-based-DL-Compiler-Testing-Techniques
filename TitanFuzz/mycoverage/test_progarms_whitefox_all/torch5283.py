import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.f = torch.nn.Sequential(torch.nn.BatchNorm2d(3))
    def forward(self, x3):
        s3 = self.f(x3)
        return s3
m = Model()
# Inputs to the model
x3 = torch.randn(6, 3, 4, 4)
