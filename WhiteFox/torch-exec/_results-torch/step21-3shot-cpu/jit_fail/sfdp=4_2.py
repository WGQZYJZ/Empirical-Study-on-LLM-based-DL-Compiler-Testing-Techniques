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

    def __init__(self, embed_dims, num_heads, qkv_bias, qk_scale, dropout_ratio):
        super().__init__()
        self.embed_dims = embed_dims
        self.num_heads = num_heads
        self.scale = qk_scale or self.embed_dims ** (-0.5)
        self.qkv = torch.nn.Linear(in_features=embed_dims, out_features=embed_dims * 3, bias=qkv_bias)
        self.attn_drop = torch.nn.Dropout(dropout_ratio)
        self.proj = torch.nn.Linear(in_features=embed_dims, out_features=embed_dims)
        self.proj_drop = torch.nn.Dropout(dropout_ratio)

    def forward(self, qkv):
        (q, k, v) = torch.chunk(self.qkv(qkv), 3, dim=-1)
        attn = q @ k.transpose(-2, -1) * self.scale
        attn = attn.softmax(dim=-1)
        attn = self.attn_drop(attn)
        x = (attn @ v).transpose(1, 2).reshape(qkv.shape)
        x = self.proj(x)
        x = self.proj_drop(x)
        return x


embed_dims = 1
num_heads = 1
qkv_bias = 1
qk_scale = 1
dropout_ratio = 1

func = Model(embed_dims, num_heads, qkv_bias, qk_scale, dropout_ratio).to('cpu')


qkv = torch.randn(4, 128, 64)

test_inputs = [qkv]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (512x64 and 1x3)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(4, 128, 64)), Parameter(FakeTensor(..., size=(3, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [512, 64] X [1, 3].

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''