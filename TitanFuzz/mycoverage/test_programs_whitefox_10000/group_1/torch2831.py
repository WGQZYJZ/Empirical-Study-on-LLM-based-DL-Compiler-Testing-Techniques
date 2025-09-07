import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x):
        return torch.clamp_max(self.leaky_relu(torch.mean(torch.abs(x), dim=(2, 3), keepdim=True)), max=1.3)
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 64, 64)
