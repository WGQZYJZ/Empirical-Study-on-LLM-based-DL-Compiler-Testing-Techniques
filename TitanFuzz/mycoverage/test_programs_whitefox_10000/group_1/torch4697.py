import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
  
    def forward(self, input):
        q = input
        k = input
        output = torch.matmul(q, k.transpose(-2, -1))
        return output

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
input = torch.randn(1, 200, 64)
