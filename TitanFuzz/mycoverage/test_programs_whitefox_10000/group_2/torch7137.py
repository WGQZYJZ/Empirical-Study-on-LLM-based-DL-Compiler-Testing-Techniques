import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x_1, x_2, x_3):
        v1 = x_1 + x_2 * x_3
        return v1

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x_1 = torch.randn(128, 20)
x_2 = torch.randn(64, 20)
x_3 = torch.randn(20, 32)
