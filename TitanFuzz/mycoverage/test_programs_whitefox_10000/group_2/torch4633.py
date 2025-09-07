import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x = torch.cat((torch.cat((x, x)), x), dim=0)
        x = x.squeeze(dim=1).view(x.shape[0], -1)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 3, 4)
