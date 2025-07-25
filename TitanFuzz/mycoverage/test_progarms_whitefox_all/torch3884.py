import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 3)
    def forward(self, x):
        x = self.layers(x)
        if not None: 
            x = x.flatten(1)
        x = torch.stack((x, x), dim=1)
        x = torch.cat((x, x, x, x), dim=1)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
