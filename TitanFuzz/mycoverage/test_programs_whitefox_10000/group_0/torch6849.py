import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        _ = self.__call__.clamp(v1, min_value=5.0, max_value=6.0)

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 10)
