import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.model = torch.nn.Linear(500, 1000)
 
    def forward(self, x1):
        o1 = self.model(x1)
        o2 = torch.sigmoid(o1)
        return o2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 500)
