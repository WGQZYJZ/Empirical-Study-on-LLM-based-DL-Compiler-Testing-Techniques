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



class SelfAttention(torch.nn.Module):

    def __init__(self, dim, num_heads=1, qkv_bias=False, qk_scale=None, dropout_p=0.0):
        super().__init__()
        self.num_heads = num_heads
        self.dim = dim
        self.head_dim = (dim // num_heads)
        self.scale = (qk_scale or (self.head_dim ** (- 0.5)))
        self.qkv = torch.nn.Linear(dim, (dim * 3), bias=qkv_bias)
        self.dropout = torch.nn.Dropout(dropout_p)
        self.proj = torch.nn.Linear(dim, dim)

    def forward(self, x):
        b = x.shape[0]
        qkv = self.qkv(x).reshape(b, (- 1), 3, self.num_heads, self.head_dim).permute(2, 0, 3, 1, 4)
        q = qkv[0]
        k = qkv[1]
        v = qkv[2]
        attn = ((q @ k.transpose((- 2), (- 1))) * self.scale)
        attn = attn.softmax(dim=(- 1))
        attn = self.dropout(attn)
        x = (attn @ v).transpose(1, 2).reshape(b, (- 1), self.dim)
        x = self.proj(x)
        return x



dim = 1

func = SelfAttention(dim).to('cuda')



x1 = torch.randn(1, 4, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x5 and 1x3)

jit:
Failed running call_module L__self___qkv(*(FakeTensor(..., device='cuda:0', size=(1, 4, 5)),), **{}):
a and b must have same reduction dim, but got [4, 5] X [1, 3].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''