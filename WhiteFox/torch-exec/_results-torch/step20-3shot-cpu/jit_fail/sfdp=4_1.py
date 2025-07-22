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

    def __init__(self, embed_dim, num_heads, dropout=0.0):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.dropout = dropout
        self.head_dim = embed_dim // num_heads
        self.scaling = self.head_dim ** (-0.5)
        self.k_proj = torch.nn.Linear(embed_dim, embed_dim)
        self.v_proj = torch.nn.Linear(embed_dim, embed_dim)
        self.q_proj = torch.nn.Linear(embed_dim, embed_dim)
        self.out_proj = torch.nn.Linear(embed_dim, embed_dim)

    def forward(self, k, v, q, attn_mask=None):
        bs = k.size(0)
        l = k.size(1)
        k = self.k_proj(k)
        v = self.v_proj(v)
        q = self.q_proj(q)
        q = q * self.scaling
        k = k.view(bs, l, self.num_heads, self.head_dim).transpose(1, 2)
        v = v.view(bs, l, self.num_heads, self.head_dim).transpose(1, 2)
        q = q.view(bs, l, self.num_heads, self.head_dim).transpose(1, 2)
        attn_score = torch.matmul(q, k.transpose(-2, -1))
        attn_score = attn_score.masked_fill(attn_mask, float('-inf'))
        attn_weight = torch.softmax(attn_score, dim=-1)
        attn_weight = F.dropout(attn_weight, p=self.dropout, training=self.training)
        attn_out = torch.matmul(attn_weight, v)
        attn_out = attn_out.transpose(1, 2).contiguous().view(bs, l, self.embed_dim)
        attn_out = self.out_proj(attn_out)
        return attn_out


embed_dim = 1
num_heads = 1

func = MultiheadAttention(embed_dim, num_heads).to('cpu')


k = torch.randn(1, 64, 64)

v = torch.randn(1, 64, 64)

q = torch.randn(1, 64, 64)

test_inputs = [k, v, q]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (64x64 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 64, 64)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [64, 64] X [1, 1].

from user code:
   File "<string>", line 30, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''