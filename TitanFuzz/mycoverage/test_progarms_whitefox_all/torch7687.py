import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU6()
    def forward(self, x):
        return self.relu(x)
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 224, 224)
