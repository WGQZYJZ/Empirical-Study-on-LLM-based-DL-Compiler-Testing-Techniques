import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        v1 = torch.cat([x, x, x])
        v1.reshape(v1.shape[0], -1).relu().tanh()
        return v1
m = Model()
# Inputs to the model
x = torch.randn(3, 2, 3)
