import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, K9, Q, V3, mask):
        qk = Q @ K9.transpose(-2, -1) / math.sqrt(Q.size(-1))
        qk = qk + mask
        output = qk @ V3
        return output
m = Model()
# Inputs to the model
Q = torch.randn(1, 64, 56, 56)
K = torch.randn(1, 64, 56, 56)
V = torch.randn(1, 64, 56, 56)
mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
