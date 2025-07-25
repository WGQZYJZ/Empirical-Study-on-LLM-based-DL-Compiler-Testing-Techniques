import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=0.5)
        v3 = torch.clamp_max(v2, max_value=1)
        return torch.reshape(v3, [64, 8])
    #TODO: Fill __input__/__output__.

m = Model()
# Initializing the model
m = Model()

__input__ = torch.randn(1, 8)
