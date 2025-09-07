

import torch, sys, string
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):
        return t1  # Returning the tensor back unmodified

t = torch.randn((2, 2))
m  = sys.modules[__name__]

