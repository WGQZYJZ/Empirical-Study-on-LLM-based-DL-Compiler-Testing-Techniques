
import torch
import math
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):  # A PyTorch implementation of a scaled dot-product attention layer
        k = key.transpose(-2, -1) / math.sqrt(key.size(-1))
        k += attn_mask if (attn_mask is not None) else torch.zeros_like(k)
        weight = torch.softmax(k, dim=-1)
        return  weight @ value


m = Model()
q = torch.randn(32, 64, 500) # The query tensor with shape (batch size, number of heads, sequence length)
k = torch.randn(32, 64, 500) # The key tensor with shape (batch size, number of heads, sequence length)
v = torch.randn(32, 64, 512) # The value tensor with shape (batch size, number of heads, sequence length)

