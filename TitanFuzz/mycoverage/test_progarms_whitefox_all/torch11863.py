import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, Q, K, v, M):
        qk = Q @ K.transpose(-2, -1) / math.sqrt(Q.size(-1))
        qk = qk + M
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ V
        return output
m = Model()
# Inputs to the model
Q = torch.randn(1, 64, 56, 56)
K = torch.randn(1, 64, 56, 56)
V = torch.randn(1, 64, 56, 56)
mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
