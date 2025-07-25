import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,5)
 
    def forward(self, l):
        l1 = self.linear(l)
        l2 = l1 + 3
        l3 = torch.clamp_min(l2, 0)
        l4 = torch.clamp_max(l3, 6)
        l5 = l4 / 6
        return l5

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.tensor([[1, 2, 3], [4, 5, 6]], requires_grad=True)
