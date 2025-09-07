import torch
from torch import nn



import torch.nn as nn


class Model(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x3):
        return x3


m = Model()
# Inputs to the model
x3 = torch.randn(1, 16, 16, 3)
