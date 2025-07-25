import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, Q7, KK7, VV3, mask):
        qk = Q7 @ KK7.transpose(-2, -1) / math.sqrt(Q7.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ VV3
        return output
m = Model()
# Inputs to the model
Q5 = torch.randn(1, 64, 56, 56)
K5 = torch.randn(1, 64, 56, 56)
V5 = torch.randn(1, 64, 56, 56)
mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
