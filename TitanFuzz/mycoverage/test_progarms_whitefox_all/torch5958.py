import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 2)
    def forward(self, x):
        x = self.layers(x)
        x = x * x
        x = torch.tanh(x)
        x = x * x
        x = torch.sigmoid(x)
        x = torch.cat((x, x), dim=1)
        x = torch.stack((x, x, x, x), dim=1).view(x.shape[0], -1)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
