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

class SelfAttention(nn.Module):

    def __init__(self, dim, heads, dropout):
        super().__init__()
        self.heads = heads
        self.v_head = dim // heads
        self.dropout = nn.Dropout(dropout)
        self.to_q_k = nn.Linear(dim, dim * 2, bias=False)
        self.to_dense = nn.Linear(dim, dim)

    def forward(self, x):
        (b, t, d) = x.size()
        kv = self.to_q_k(x).chunk(2, dim=-1)
        k = kv[0].transpose(1, 2)
        v = kv[1]
        scale_factor = 1 / (d * (d - 1) / 2) ** 0.5
        q = k @ v.transpose(-1, -2) * scale_factor
        q = q.softmax(dim=-1) @ v
        q = q.transpose(0, 1).chunk(self.heads, dim=0)
        q = torch.stack(q, dim=1)
        q = q.transpose(1, 2).reshape(b, t, d)
        q = self.dropout(q)
        return self.to_dense(q)


dim = 1
heads = 1
dropout = 1

func = SelfAttention(dim, heads, dropout).to('cpu')


x1 = torch.randn(32, 10, 512)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (320x512 and 1x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(32, 10, 512)), Parameter(FakeTensor(..., size=(2, 1), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [320, 512] X [1, 2].

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''