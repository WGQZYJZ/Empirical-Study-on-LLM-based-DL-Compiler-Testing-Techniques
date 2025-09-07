import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(16, 3, 3, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.convt(x)
        return torch.sigmoid(v1)

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 16, 64, 64)
