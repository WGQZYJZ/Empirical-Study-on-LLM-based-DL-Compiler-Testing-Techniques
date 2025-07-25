import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        activation = torch.sigmoid(v1).unsqueeze(-1)
        return activation

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64)
