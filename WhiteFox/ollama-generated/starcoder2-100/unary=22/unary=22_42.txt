

import torch
from torch import nn  # noqa F811: Import not used
class Model(nn.Module):
    def __init__(self, *args):
        super().__init__()
        self._linear = nn.Linear(*args)
 
    @property
    def linear(self):
        return self._linear
 
    @linear.setter
    def linear(self, value):
        self._linear  = value
        
    def forward(self, x1):
        return torch.tanh(self.linear(x1))

# Initializing the model with two parameters
m  = Model(32768 , 5)

 # Inputs to the model
x1   = [torch.randn(size=(24576, 3))]
 
 # Outputs from the model: A single output tensor of shape (24576,)
