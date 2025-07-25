import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.f1 = torch.nn.Linear(12, 8)

    def forward(self, x1):
        v1 = torch.sigmoid(self.f1(x1))
        v2 = self.f1(x1) * v1
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 12)
