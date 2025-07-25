import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=0)
    def forward(self, x1):
        v1 = self.conv1(x1)
        return v1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 224, 224)
# Inputs for checking the model
dummy_input = torch.randn(1, 3, 224, 224)
