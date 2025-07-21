import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Conv2d(3, 20, 18, stride=(3, 2), padding=(1, 2))
 
    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = torch.tanh(v1)
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
