

import torch  # noqa: F401
from torch import nn
 
 
class Model(nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = nn.functional.conv_transpose2d(x1)
        return nn.functional.sigmoid(v1)

 # Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(308, 7459, 6, 6)
__output__  = m(x1).sum().item() == 0.0 # noqa: F821
 