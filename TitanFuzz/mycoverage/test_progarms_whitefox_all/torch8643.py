import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v3 = v1 + (v1 * v1 * v1) * 0.044715
        v2 = v3 * 0.7978845608028654
        v4 = torch.tanh(v2)
        v5 = v4 + 1
        v6 = v1 * v5
        return v6

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
