import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, q7, k, v0, mask):
        qk = q7 @ k.transpose(-2, -1) / math.sqrt(q7.size(-1))
        qk = qk + mask
        m = torch.nn.Softmax(qk, dim = -2)
        output = torch.mm(m, v0)
        return output
m = Model()
# Inputs to the model
Q = torch.randn(1, 64, 56, 56)
K = torch.randn(1, 64, 56, 56)
V = torch.randn(1, 64, 56, 56)
mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
