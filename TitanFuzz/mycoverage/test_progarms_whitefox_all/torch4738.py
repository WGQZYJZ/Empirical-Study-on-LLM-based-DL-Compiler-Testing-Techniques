import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        x = torch.addmm(input=x, mat1=torch.randn(2, 2), mat2=torch.randn(2, 2))
        return x
m = Model()
# Input to the model
x = torch.randn(1, 2)
