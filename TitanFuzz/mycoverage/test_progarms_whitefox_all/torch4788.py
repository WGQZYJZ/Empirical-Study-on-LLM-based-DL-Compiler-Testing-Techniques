import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x, k2, v, mask):
        qk = x @ k2.transpose(-2, -1) / math.sqrt(x.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v
        return output
m = Model()
# Inputs to the model
Q = torch.randn(1, 192, 56, 56)
K = torch.randn(1, 192, 56, 56)
V = torch.randn(1, 192, 56, 56)
mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
