import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, inputs):
        v1 = torch.mm(inputs, inputs)
        v2 = torch.mm(inputs, inputs)
        v3 = torch.mm(inputs, inputs)
        v4 = torch.mm(inputs, inputs)
        v5 = v1 + v2 + v3
        return v4 + v5 + v1 + v3
m = Model()
# Inputs to the model
inputs = torch.randn(4, 4)
