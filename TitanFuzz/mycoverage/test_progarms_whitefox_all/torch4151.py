import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)
        self.other = torch.zeros(8)

    def forward(self, x1):
        t1 = self.linear(x1)
        t2 = t1 - self.other
        t3 = torch.nn.functional.relu(t2)

        return t3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4)
