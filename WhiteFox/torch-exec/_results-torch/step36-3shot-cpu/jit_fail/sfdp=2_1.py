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

    def __init__(self, dim, heads):
        super().__init__()
        self.num_heads = heads
        self.dim_per_head = dim // heads
        self.qkv_dim = self.num_heads * self.dim_per_head
        self.linear0 = torch.nn.Linear(dim, self.qkv_dim * 3)
        self.linear1 = torch.nn.Linear(self.qkv_dim * 3, dim)

    def forward(self, x, mask=None):
        if mask is not None:
            mask = mask.unsqueeze(1).unsqueeze(2).float().to(x.device)
        head_qkv = self.linear0(x).reshape((self.num_heads, -1, 3, self.dim_per_head)).permute(0, 2, 1, 3)
        (query, key, value) = head_qkv.split((self.dim_per_head,) * 3, dim=-1)
        qk = torch.matmul(query, key.transpose(-2, -1))
        qk = qk * self.dim_per_head ** (-0.5)
        if mask is not None:
            qk += (mask * -1e+30).to(qk.dtype)
        qk = torch.softmax(qk, dim=-1)
        head_v = self.linear1(qk.matmul(value.reshape((self.num_heads, -1, self.dim_per_head))).reshape((self.num_heads, -1, self.dim_per_head * 2))).reshape((self.num_heads, -1, self.dim_per_head))
        return value + head_v.permute(0, 2, 1, 3).reshape((self.num_heads * self.dim_per_head, -1, self.dim_per_head))


dim = 1
heads = 1
func = Model(512, 8).to('cpu')


x = torch.randn(64, 80, 512)
x = torch.randn(64, 80, 512)

mask = torch.ones(x.shape[0], 80, 80)

test_inputs = [x, mask]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 64 (input tensor's size at dimension -1), but got split_sizes=[64, 64, 64]

jit:
Failed running call_method split(*(FakeTensor(..., size=(8, 3, 5120, 64)), (64, 64, 64)), **{'dim': -1}):
Split sizes add up to 192 but got the tensor's size of 64

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''