import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:112]
        v4 = torch.cat([v1, v3], dim=1)
        return self.relu(v4)
    
m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 128, 4, 4)
x2 = torch.randn(1, 456, 8, 8)
