
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = v1 + 3
        v3  = F.clamp(v2, min=0)
        v4  = F.clamp(v3, max=6)
        v5  = v1 * v4
        v6  = v5 / 6
        return v6


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 8, 27, 30)
__output__  = m(x1)

<|model|end_of_model|>

import torch
from torch import nn


# Model definition
class Model(nn.Module):
    def __init__(self):
        super().__init__()

        self.linear1 = nn.Linear(in_features=5, out_features=4)

    def forward(self, x: torch.Tensor):
        output = self.linear1(x) + 1
        return output

model = Model()

