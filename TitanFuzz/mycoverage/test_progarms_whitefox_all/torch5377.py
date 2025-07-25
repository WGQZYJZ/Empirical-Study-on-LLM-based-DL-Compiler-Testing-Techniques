import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2, inp):
        v1 = torch.mv(x1, inp)
        return torch.dot(v1, x2)
m = Model()
# Inputs to the model
inp = torch.randn(3, 3)
x1 = inp.transpose(1,0)
x2 = torch.randn(3, 3)
