import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)
    def forward(self, l1):
        return l1
m = Model()
m = Model()

# Input to the model
__input__ = torch.randn(1, 10)
