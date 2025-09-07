import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 4)
 
    def forward(self, x2):
        t1 = self.linear(x2)
        t2 = torch.sigmoid(t1)
        t3 = t1 * t2
        return t3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 8)
