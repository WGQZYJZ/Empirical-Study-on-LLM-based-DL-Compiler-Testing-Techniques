import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.negative_slope = negative_slope
        self.fc = torch.nn.Linear(10, 10)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4
        
m = Model()
# Initializing the model
m = Model(1)

# Inputs to the model
x1 = torch.randn(12, 10)
