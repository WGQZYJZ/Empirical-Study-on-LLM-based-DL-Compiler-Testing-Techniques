import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg

class MultiheadAttention(torch.nn.Module):

    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_model = d_model
        self.depth = d_model // self.num_heads

    def _split_heads(self, x):
        (B, T, D) = x.shape
        x = x.view(B, T, self.num_heads, self.depth)
        return x.transpose(1, 2).contiguous()

    def forward(self, q, k, v, mask):
        query = self._split_heads(q)
        key = self._split_heads(k)
        value = self._split_heads(v)
        query = query * int(self.d_model) ** (-0.5)
        key = key * int(self.d_model) ** (-0.5)
        attn_logits = torch.matmul(query, key.transpose(-2, -1))
        if mask is not None:
            attn_logits = attn_logits + mask
        attn_weights = F.softmax(attn_logits, dim=-1)
        attn = torch.matmul(attn_weights, value)
        attn = attn.transpose(1, 2).contiguous()
        attn = attn.view(B, -1, self.num_heads * self.depth)
        output = attn
        return output


d_model = embed_dim * num_heads
num_heads = 4
func = MultiheadAttention(d_model, num_heads).to('cpu')


embed_dim = 8
q = torch.randn(4, 5, embed_dim)

embed_dim = 8
k = torch.randn(4, 4, embed_dim)

embed_dim = 8
v = torch.randn(4, 4, embed_dim)
mask = 1

test_inputs = [q, k, v, mask]
