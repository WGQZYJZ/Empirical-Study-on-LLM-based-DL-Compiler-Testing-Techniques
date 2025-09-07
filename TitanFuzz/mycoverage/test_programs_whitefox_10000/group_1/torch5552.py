import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64 * 3, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
__input_tensor__ = torch.randn(1, 64 * 64 * 3)
