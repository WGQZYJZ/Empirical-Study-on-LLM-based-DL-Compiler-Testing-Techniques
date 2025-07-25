import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 3, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.convt(x)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
