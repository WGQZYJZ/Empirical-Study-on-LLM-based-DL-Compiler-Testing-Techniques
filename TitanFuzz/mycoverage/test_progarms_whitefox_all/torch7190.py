import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, __other__=torch.randn(1, 8)):
        t1 = self.linear(x1)
        t2 = t1 + __other__
        return t2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
