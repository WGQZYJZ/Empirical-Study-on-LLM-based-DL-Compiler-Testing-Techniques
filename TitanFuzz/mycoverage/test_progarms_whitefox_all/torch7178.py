import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(4, 3)
    def forward(self, x):
        x = self.layers(x)
        x = torch.stack((x, x, x, x), dim=1)
        x = torch.cat((x, x), dim=2)
        x = torch.sum(x, dim=2).view(x.shape[0], -1)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 4)
