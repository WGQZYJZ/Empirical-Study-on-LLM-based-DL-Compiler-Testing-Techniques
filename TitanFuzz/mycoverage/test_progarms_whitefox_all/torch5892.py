import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        y = torch.cat((x, x), dim=1).view(-1)
        x = y.tanh() if (x.shape[1], x.shape[0])!= (6, 2) else y.tanh()
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 3, 4)
