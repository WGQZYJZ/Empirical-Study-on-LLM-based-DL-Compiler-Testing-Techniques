import torch
from torch import nn

class Model(torch.nn.Module):
    pass

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 256, 4)
x2 = torch.randn(1, 8, 128, 8)
x3 = torch.randn(1, 8, 64, 16)
