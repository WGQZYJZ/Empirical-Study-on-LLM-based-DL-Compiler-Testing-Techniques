import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, query_tensor, key_tensor, value_tensor, mask1):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + mask1
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output
m = Model()
# Inputs to the model
Q = torch.randn(1, 64, 56, 56)
K = torch.randn(1, 64, 56, 56)
V = torch.randn(1, 64, 56, 56)
mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
