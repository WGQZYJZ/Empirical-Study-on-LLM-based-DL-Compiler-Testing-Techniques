import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.tanh(v1)
        return v2

m = Model()
# Initializing the model
m = model.Model()

# Inputs to the model
x1 = torch.randn(1, 28 * 28)
