import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.heads = 503
        self.seq_len = 4404
        self.dim = 12
    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, 0.1, True)
        output = attn_weight @ value
        return output
m = Model()
# Inputs to the model
query = torch.randn(1, 503, 4404, 12)
key = torch.randn(1, 503, 4404, 12)
value = torch.randn(1, 503, 4404, 12)
attn_mask = torch.randn(1, 1, 4404, 4404)
