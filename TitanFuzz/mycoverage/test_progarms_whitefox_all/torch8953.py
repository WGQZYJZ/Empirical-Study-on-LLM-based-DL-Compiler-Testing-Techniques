import torch
from torch import nn

class Model(torch.nn.Module):
  def __init__(self):
    super().__init__()
    self.linear = torch.nn.Linear(in_features=10, out_features=5)
    self.negative_slope = 0.1
 
  def forward(self, x1):
    v1 = self.linear(x1)
    v2 = v1 > 0
    v3 = v1 * self.negative_slope
    v4 = torch.where(v2, v1, v3)
    return v4

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 10)
