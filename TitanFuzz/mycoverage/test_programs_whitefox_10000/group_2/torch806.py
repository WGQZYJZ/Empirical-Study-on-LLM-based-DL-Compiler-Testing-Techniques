import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self):
        return torch.ones(5, 5, dtype=torch.float)

m = Model()
model = Model()
# Input to the model
input1 = torch.randn(5, 5)
