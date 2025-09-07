import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax = torch.nn.Softmax(dim=-1)
    def forward(self, x):
        return self.softmax(x)
m = Model()
# Inputs to the model
x = torch.randn(3, 5)
