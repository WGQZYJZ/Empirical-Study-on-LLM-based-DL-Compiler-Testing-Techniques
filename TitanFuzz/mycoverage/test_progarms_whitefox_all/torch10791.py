import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 100, bias=False)
        self.other = torch.ones((100,), dtype=torch.float32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + self.other

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 100)
