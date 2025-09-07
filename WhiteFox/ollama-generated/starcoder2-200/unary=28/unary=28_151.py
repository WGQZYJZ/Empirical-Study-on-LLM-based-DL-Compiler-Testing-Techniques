
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1): 
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = torch.clamp_min(v1, -0.75) # Clamp the output of the linear transformation to a minimum value (-0.75 in this case)
        v3 = torch.clamp_max(v2, 0.8695834107337236) # Clamp the output of the previous operation to a maximum value (in this case 0.8695834107337236)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
__output__  = m(x1)

<model.py>
import torch
import numpy as np
 
class LayerNorm(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensor): 
        v1 = input_tensor # The input tensor is passed through the layer normalization operation
        return v1
 
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv  = torch.nn.Conv2d(3, 8, 5)
        self.lin   = LayerNorm()
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply a pointwise convolution to the input tensor
        v2 = self.lin(v1) # Apply layer normalization to the output of the convolution operation
        return v2
 
m  = Model()

