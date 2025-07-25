import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        y = torch.cat((x, x + 1.0), dim=1)
        return y.view(y.shape[0], -1).tanh() if y.shape!= (1, 3) else y.view(y.shape[0], -1).relu()
m = Model()
# Inputs to the model
x = torch.randn(2, 2, 2)
