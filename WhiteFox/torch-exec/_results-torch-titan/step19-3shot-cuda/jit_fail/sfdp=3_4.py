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



class MultiheadScaledDotProductAttention(torch.nn.Module):

    def __init__(self, dim, num_heads):
        super().__init__()
        if (((dim % num_heads) != 0) or (num_heads <= 0)):
            raise ValueError(f'The feature dimension {dim} should be divisible by the number of heads {num_heads}.')
        self.dim = dim
        self.num_heads = num_heads
        self.head_dim = (dim // num_heads)
        self.queries = torch.nn.Linear(dim, dim)
        self.keys = torch.nn.Linear(dim, dim)
        self.values = torch.nn.Linear(dim, dim)
        self.out = torch.nn.Linear(dim, dim)
        self.softmax = torch.nn.Softmax(dim=(- 1))

    def forward(self, query, key, value, mask=None, dropout_p=0.1):
        batch_size = query.size(0)
        query_proj = self.queries(query)
        key_proj = self.keys(key)
        value_proj = self.values(value)
        query_pairs = query_proj.view(batch_size, (- 1), self.num_heads, self.head_dim).transpose(1, 2)
        key_pairs = key_proj.view(batch_size, (- 1), self.num_heads, self.head_dim).transpose(1, 2)
        value_pairs = value_proj.view(batch_size, (- 1), self.num_heads, self.head_dim).transpose(1, 2)
        q = query_pairs.query
        k = key_pairs.key
        v = value_pairs.value
        attn = ((q @ k.transpose((- 2), (- 1))) * (self.head_dim ** (- 0.5)))
        if (mask is not None):
            attn = attn.masked_fill((mask == 0), (- 1000000000.0))
        scaled_attn = attn.softmax(dim=(- 1))
        attn_drop = torch.nn.functional.dropout(scaled_attn, p=dropout_p)
        out = (attn_drop @ v)
        out_pairs = torch.cat([out_i.unsqueeze(2) for out_i in torch.split(out, batch_size, dim=0)], dim=2)
        out = out_pairs.out
        return out



dim = 1
num_heads = 1

func = MultiheadScaledDotProductAttention(dim, num_heads).to('cuda')



x1 = torch.randn(20, 32, 512)



x2 = torch.randn(20, 32, 512)




mask = torch.randn(20, 1, 32, 32).to(torch.bool)

query = 1
key = 1

test_inputs = [x1, x2, mask, query, key]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (640x512 and 1x1)

jit:
Failed running call_module L__self___queries(*(FakeTensor(..., device='cuda:0', size=(20, 32, 512)),), **{}):
a and b must have same reduction dim, but got [640, 512] X [1, 1].

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''