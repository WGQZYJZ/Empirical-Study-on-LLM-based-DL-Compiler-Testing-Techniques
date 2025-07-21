import torch
from torch import nn


class Model(nn.Module):
    def forward(self, x):
        x = torch.stack((x, x, x, x), dim=1)
        x = torch.cat((x, x, x, x), dim=1)
        x = x.flatten(end_dim=-2)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
