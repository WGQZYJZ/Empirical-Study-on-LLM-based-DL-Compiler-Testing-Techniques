import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.d = torch.nn.Dropout()
    def forward(self, x):
        x = self.d(x)
        x = F.dropout(x, p=0.5)
        return x
m = Model()
# Inputs to the model
x = torch.randn(1, 1, 2)
