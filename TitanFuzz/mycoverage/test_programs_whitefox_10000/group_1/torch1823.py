import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, model_input):
        v1 = torch.mm(model_input, model_input)
        v2 = torch.mm(model_input, model_input)
        v3 = v1 + v2
        return v3
m = Model()
# Inputs to the model
model_input = torch.randn(1, 1)
