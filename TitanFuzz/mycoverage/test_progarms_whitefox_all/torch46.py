import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(3, 6, 2, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv_t(x)
        v2 = F.relu(v1)
        return v2

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
