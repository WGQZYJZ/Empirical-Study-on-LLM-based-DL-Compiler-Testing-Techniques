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

    def __init__(self, n_head, dim, d_ff):
        super().__init__()
        self.n_head = n_head
        self.dim = dim
        self.d_ff = d_ff
        self.in_linear = torch.nn.Linear(dim, d_ff)
        self.ff_linear = torch.nn.Linear(d_ff, dim)
        self.out_linear = torch.nn.Linear(dim, dim)

    def forward(self, q, k, v, attn_mask):
        n_query = q.size(1)
        q = self.in_linear(q)
        k = self.out_linear(self.in_linear(k))
        v = self.out_linear(self.in_linear(v))
        q *= self.dim ** (-0.5)
        (q, k, v) = split_heads(q, k, v, self.n_head)
        attn_mask = attn_mask.unsqueeze(1).unsqueeze(2)
        attn_mask = attn_mask.repeat(1, self.n_head, n_query, 1).unsqueeze(1)
        (q, k, v) = attn_core(q, k, v, attn_mask)
        q = merge_heads(q, self.n_head)
        q = self.ff_linear(q)
        q = self.out_linear(q)
        return q


n_head = 8
dim = 64
d_ff = 1024
func = Model(n_head, dim, d_ff).to('cpu')


dim = 64
n_query = 100
x1 = torch.randn(1, n_query, dim)

dim = 64
n_memory = 200
memory = torch.randn(1, n_memory, dim)
n_memory = 200
n_query = 100


attn_mask = torch.tril(torch.ones((1, n_query, 1, n_memory)), 0).cuda()
q = 1

test_inputs = [x1, memory, attn_mask, q]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (200x1024 and 64x64)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s2, 1024)), Parameter(FakeTensor(..., size=(64, 64), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s2, 1024] X [64, 64].

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''