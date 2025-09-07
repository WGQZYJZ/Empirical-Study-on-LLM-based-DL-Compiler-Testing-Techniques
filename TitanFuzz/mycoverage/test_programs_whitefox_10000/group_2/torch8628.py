import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(128,1)
 
    def forward(self, x1):
        return torch.sigmoid(self.fc(x1))

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 128)
