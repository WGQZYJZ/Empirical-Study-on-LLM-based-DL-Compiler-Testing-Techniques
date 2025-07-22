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

    def __init__(self, embed_dim, num_heads, dropout=0.0, bias=True):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.dropout = dropout
        self.head_dim = (embed_dim // num_heads)
        self.scaling = (self.head_dim ** (- 0.5))
        self._qkv_proj = torch.nn.Linear(embed_dim, (3 * embed_dim), bias=bias)
        self._out_proj = torch.nn.Linear(embed_dim, embed_dim, bias=bias)

    def forward(self, query, key, value, attn_mask=None, key_padding_mask=None, need_weights=False):
        (tgt_len, bsz, embed_dim) = query.size()
        (src_len, _, _) = key.size()
        qkv = self._qkv_proj(query)
        qkv = qkv.reshape(tgt_len, (bsz * self.num_heads), (3 * self.head_dim)).transpose(0, 1)
        (query, key, value) = qkv.split([self.head_dim, self.head_dim, self.head_dim], dim=(- 1))
        attn_weight = ((query @ key.transpose((- 2), (- 1))) * self.scaling)
        attn_weight_float = torch.where((attn_weight == 0), torch.tensor(float('-Inf')).to(torch.double), attn_weight)
        attn_mask = torch.where((attn_mask == 0), 0, (attn_mask * (- 10000.0)))
        attn_weight = (attn_weight_float + attn_mask)
        attn_weight = torch.where((key_padding_mask.transpose((- 2), (- 1)) == 0), attn_weight, torch.tensor(float('-Inf')).to(torch.double))
        attn_weight = torch.softmax(attn_weight, dim=(- 1))
        attn_weight = self.dropout(attn_weight)
        attn_output = (attn_weight @ value)
        attn_output = attn_output.transpose(0, 1).reshape(bsz, tgt_len, self.embed_dim)
        attn_output = self._out_proj(attn_output)
        return attn_output



embed_dim = 1
num_heads = 1

func = MultiheadAttention(embed_dim, num_heads).to('cuda')



src = torch.randn(20, 32, 16)

query = 1
key = 1
value = 1

test_inputs = [src, query, key, value]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'size'

jit:
'int' object has no attribute 'size'

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''