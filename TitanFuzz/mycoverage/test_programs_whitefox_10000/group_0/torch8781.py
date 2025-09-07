import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(20, 10)
        self.linear2 = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        lin = self.linear1(x1)
        non_linear = relu(lin)
        return non_linear

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 20)
