import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.heads = 8
        self.seq_len = 484
        self.dim = 96 // self.heads
    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, 0.003, True)
        output = attn_weight @ value
        return output
m = Model()
# Inputs to the model
batch_size = 1
heads = 8
seq_len = 520
dim = 16
query = torch.randn(batch_size, heads, seq_len, dim)
key = torch.randn(batch_size, heads, seq_len, dim)
value = torch.randn(batch_size, heads, seq_len, dim)
attn_mask = torch.randn(batch_size, 1, seq_len, seq_len)
