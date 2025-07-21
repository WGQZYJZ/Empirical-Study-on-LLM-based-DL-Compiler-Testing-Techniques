import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l = torch.nn.LayerNorm(2,elementwise_affine=True)
    def forward(self, x):
        return self.l(x)
m = Model()
# Inputs to the model
x = torch.ones(1, 2, 10, 20)
