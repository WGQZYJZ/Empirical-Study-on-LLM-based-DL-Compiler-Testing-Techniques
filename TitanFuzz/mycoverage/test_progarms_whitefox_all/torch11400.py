import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:3]
        t4 = torch.cat([t1, t3], dim=1)
        return t4

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 128, 256)
x2 = torch.randn(1, 127, 254)
