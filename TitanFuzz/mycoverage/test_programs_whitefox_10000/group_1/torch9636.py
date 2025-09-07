import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        aaab = torch.cat((x, x), dim=0)
        c = aaab.tanh()
        x = c.view(c.shape[1], c.shape[0])
        return x
m = Model()
# Inputs to the model
x = torch.randn(3, 5)
