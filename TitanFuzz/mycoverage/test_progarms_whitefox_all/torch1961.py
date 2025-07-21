import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, inp):
        v1 = torch.mul(torch.mul(input1, input2), input3) # Multiply three input tensors
        v2 = v1 ** 2 # Square the result
        return v2
m = Model()
# Inputs to the model
inp = torch.randn(6)
