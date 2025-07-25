import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, query, key, value, mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output
m = Model()
# Inputs to the model
q = torch.randn(1, 64, 56, 56)
k = torch.randn(1, 64, 56, 56)
v3 = torch.randn(1, 64, 56, 56)
mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
