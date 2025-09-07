import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(13, 17)
 
    def forward(self, v1):
        return self.linear(v1) * torch.sigmoid(self.linear(v1))

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
v1 = torch.randn(1, 13)
