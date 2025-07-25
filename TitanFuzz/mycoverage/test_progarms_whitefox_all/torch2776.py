import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(8, 8)
 
    def forward(self, x1, **kwargs):
        v1 = self.fc(x1, **kwargs)
        v2 = v1 + kwargs["other"]
        v3 = torch.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
other = torch.randn(1, 8)
