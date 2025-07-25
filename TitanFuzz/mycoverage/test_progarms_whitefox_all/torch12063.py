import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, 0.)
        v3 = torch.clamp_max(v2, 0.1)
        return v3

m = Model()
# Initializing the model
m = Model()

