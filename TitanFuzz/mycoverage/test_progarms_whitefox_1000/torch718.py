import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat((x1, x2), 1)

m = Model()