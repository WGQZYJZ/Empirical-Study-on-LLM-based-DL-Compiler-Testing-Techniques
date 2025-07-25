import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16)
 
    def forward(self, x1):
        m1 = self.linear(x1)
        m2 = m1 + 3
        m3 = torch.clamp_min(m2, 0.0)
        m4 = torch.clamp_max(m3, 6.0)
        m5 = m4 / 6
        return m5

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
