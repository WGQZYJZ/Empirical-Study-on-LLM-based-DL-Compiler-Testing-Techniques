import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        y = x
        for i in range(3):
            y = torch.cat((y, y, y), dim=1)
            y = y.view(y.shape[0], -1)
            y = torch.relu(y)
        return y
m = Model()
# Inputs to the model
x = torch.randn(2, 3, 4)
