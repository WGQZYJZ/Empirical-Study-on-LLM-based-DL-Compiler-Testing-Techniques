import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU6(inplace=True)
    def forward(self, x1):
        v1 = self.relu(x1)
        v2 = 3 + v1
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v1 * v4
        v6 = v5 / 6
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 224, 224)
