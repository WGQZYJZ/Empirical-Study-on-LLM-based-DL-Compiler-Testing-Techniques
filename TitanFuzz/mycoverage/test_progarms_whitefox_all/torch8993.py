import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.heads = 192
        self.seq_len = 128
        self.dim = 2048 // self.heads
    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, 0.3, True)
        output = attn_weight @ value
        return output
m = Model()
# Inputs to the model
query = torch.randn(1, 192, 128, 2048)
key = torch.randn(1, 192, 128, 2048)
value = torch.randn(1, 192, 128, 2048)
attn_mask = torch.randn(1, 1, 128, 128)
