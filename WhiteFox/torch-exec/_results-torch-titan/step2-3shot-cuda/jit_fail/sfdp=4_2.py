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



class Model(torch.nn.Module):

    def __init__(self, n_head, dim_q, dim_k, dim_v, dim_o, dropout, attn_mask):
        super().__init__()
        self.dim_k = dim_k
        self.dim_v = dim_v
        self.dim_o = dim_o
        self.dim_total = ((dim_q + dim_k) + dim_v)
        self.w_qkv = torch.nn.Linear(dim_q, (n_head * self.dim_total), bias=False)
        self.proj = torch.nn.Linear((n_head * self.dim_total), dim_o, bias=False)
        self.attn_mask = attn_mask
        self.dropout = torch.nn.Dropout(dropout)

    def forward(self, q, k, v):
        qkv = self.w_qkv(q)
        qs = qkv[:, :, :self.dim_q].contiguous().view(q.size(0), (- 1), self.dim_q)
        ks = qkv[:, :, self.dim_q:(self.dim_k + self.dim_q)].contiguous().view(k.size(0), (- 1), self.dim_k)
        vs = qkv[:, :, (self.dim_k + self.dim_q):].contiguous().view(v.size(0), (- 1), self.dim_v)
        at = ((qs @ ks.transpose((- 2), (- 1))) / math.sqrt(self.dim_q))
        at = (at + self.attn_mask)
        at = (at / at.sum((- 1), keepdim=True).clamp(min=0))
        at = at.masked_fill(self.attn_mask.to(torch.bool), (- 1000000000.0))
        v_out = (at @ vs)
        v_out = v_out.view(v_out.size(0), (- 1))
        return self.proj(self.dropout(v_out))



n_head = 1
dim_q = 1
dim_k = 1
dim_v = 1
dim_o = 1
dropout = 1
attn_mask = 1

func = Model(n_head, dim_q, dim_k, dim_v, dim_o, dropout, attn_mask).to('cuda')

q = 1
k = 1
v = 1

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___w_qkv(*(1,), **{}):
linear(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''