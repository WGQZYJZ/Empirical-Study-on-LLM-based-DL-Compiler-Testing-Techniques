import torch
from torch import nn
 Definition
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        return v2

m = Model()
# Input tensor initialization
x1 = torch.randn(1, 64)

# Other tensor initialization
other = torch.randn(1, 64)
