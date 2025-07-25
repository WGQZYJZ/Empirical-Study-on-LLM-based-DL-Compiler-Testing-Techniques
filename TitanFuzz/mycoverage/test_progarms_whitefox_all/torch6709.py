import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10, bias=True)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + 3.0
        v3 = torch.clamp_min(v2, 0.0)
        v4 = torch.clamp_max(v3, 6.0)
        v5 = v4 / 6.0
        return v5

m = Model()
# Initializing torch random number generator
torch.random.manual_seed(0)

# Setting the input to the model
x1 = torch.randn(2, 10, requires_grad=True)
