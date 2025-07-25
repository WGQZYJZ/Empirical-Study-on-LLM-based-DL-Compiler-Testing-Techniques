import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        v1 = torch.matmul(x1.permute(0, 2, 1), x2)
        v2 = torch.matmul(x1, x2)
        v2 = v2[..., 0][..., None]
        return torch.cat((v2, v1), 1)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
