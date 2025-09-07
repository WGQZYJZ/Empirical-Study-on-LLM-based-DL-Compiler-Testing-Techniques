

import torch
import math
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = x1  * -0.49685375 + 5.27288008
        
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 1)

__output__  = m(x1).view(-1)

