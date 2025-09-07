
import torch
import torch.nn as nn
 
class M(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att = nn.MultiheadAttention(embed_dim=8, num_heads=4)
 
    def forward(self, query, key, value):
        out  = self.att(query, key)[0] 
        return out


m  = M()
 
qk = torch.rand((2, 16))
key = torch.randn([2, 8, 4]) * 357 # a random input tensor of shape [B, nk, nh]
value = torch.randn([2, 16, 4]) * 90
 
m(qk, key, value)

