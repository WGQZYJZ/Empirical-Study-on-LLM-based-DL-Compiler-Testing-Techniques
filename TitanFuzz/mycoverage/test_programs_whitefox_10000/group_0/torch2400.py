import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        z = torch.cat((x, x), dim=1)
        y = z.permute(1, 0, 2).reshape(-1, 2)
        y = y.tanh()
        return y
m = Model()
# Inputs to the model
x = torch.randn(2, 3, 4)
