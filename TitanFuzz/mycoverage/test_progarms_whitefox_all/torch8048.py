import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1):
        x2 = x1 * x1
        v1 = F.dropout(x2, p=0.4)
        return v1        
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
