import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        shape_list = list(x.shape)
        x = torch.cat([x, x, x], dim=1)
        x = torch.view(x, shape_list)
        x = torch.tanh(x)
        del shape_list
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 3, 4)
