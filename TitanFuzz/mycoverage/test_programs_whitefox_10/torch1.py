import torch
from torch import nn

def custom_model(x1, x2, p1):
    v1 = torch.mm(x1, x2)
    v2 = v1 + v1
    return v2

# Inputs to the function
x1 = torch.randn(1564, 3676)
x2 = torch.randn(3676, 32)
p1 = torch.randn(1, 1)  # Assuming p1 is a dummy tensor

# Running the custom model
output = custom_model(x1, x2, p1)
