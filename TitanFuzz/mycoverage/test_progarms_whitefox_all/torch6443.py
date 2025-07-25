import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        y1 = self.linear(x1)
        y2 = y1 * torch.clamp(torch.clamp(y1 + 3, min=0), min=0, max=6)
        y3 = y2 / 6
        return y3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(20, 3)
