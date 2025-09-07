
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         v1 = torch.nn.functional.linear(x1, self.linear.weight)
         v2  = v1.permute(0, 2, 1)
         return v2

# Initializing the model
m  = Model()

 # Inputs to the model<|end_of_code|>
import torch
from torch import nn
x1 = torch.randn(3, 4)

__output__= m(x1)