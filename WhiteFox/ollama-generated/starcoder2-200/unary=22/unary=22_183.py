import torch
from torch import nn
 
class LinearModel(nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = nn.Linear(in_features=3, out_features=1)
 
    def forward(self, x):
        y  = self.linear(x)
        z  = torch.tanh(y)
        return z
 
# Inputs to the model
x  = torch.randn(2048).reshape((16, -1))
