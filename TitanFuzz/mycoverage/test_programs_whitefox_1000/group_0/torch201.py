import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(3, 3, bias=False)
    def forward(self, x):
        x = self.layers(x)
        x = torch.cat((x, x, x, x, x), dim=1)
        return x
m = Model()
# Inputs to the model
x = torch.randn(1, 3)
