import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=3)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 13.415
        v3 = torch.nn.functional.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
