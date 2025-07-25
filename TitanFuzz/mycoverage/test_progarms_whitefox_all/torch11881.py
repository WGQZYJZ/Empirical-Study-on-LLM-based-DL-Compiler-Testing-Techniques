import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.linear = torch.nn.Linear(128, 64)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        t1 = self.linear(x1)
        t2 = t1 > 0
        t3 = t1 * self.negative_slope
        t4 = torch.where(t2, t1, t3)
        return t4

m = Model()
# Initializing the model
m = Model(negative_slope=1e-1)

# Inputs to the model
x1 = torch.randn(1, 128)
