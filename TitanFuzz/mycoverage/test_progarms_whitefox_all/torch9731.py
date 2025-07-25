import torch
from torch import nn

model = torch.nn.Sequential(
    torch.nn.Conv2d(3, 8, 1, stride=1, padding=1),
    torch.nn.Sigmoid(),
    Lambda(lambda x: x * 2),
    torch.nn.Conv2d(1, 2, 1, stride=1, padding=1))
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
