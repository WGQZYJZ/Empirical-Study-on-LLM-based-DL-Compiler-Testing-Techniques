import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 3, stride=1, padding=1)
 
    def forward(self, x):
        return torch.tanh(self.conv_transpose(x))

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 8, 64, 64)
