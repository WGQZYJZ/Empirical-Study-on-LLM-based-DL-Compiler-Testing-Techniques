import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 5)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3

m = Model()
# Initializing the model
m = Model()

# Initialize the input tensor and set the `other` tensor to be zero
x1 = torch.randn(1, 3)
other = torch.zeros(1, 5)
