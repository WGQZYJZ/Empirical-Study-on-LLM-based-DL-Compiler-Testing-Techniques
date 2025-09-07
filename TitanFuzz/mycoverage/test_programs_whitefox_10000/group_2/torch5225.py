import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(10, 20)
 
    def forward(self, x):
        v1 = torch.tanh(self.fc(x))
        return v1

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 10)
