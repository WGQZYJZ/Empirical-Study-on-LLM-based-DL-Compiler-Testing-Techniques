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

    def __init__(self, embed_dim, num_heads, dropout=0.1):
        super().__init__()
        self.num_heads = num_heads
        self.embed_dim = embed_dim
        self.k_proj = torch.nn.Linear(embed_dim, embed_dim)
        self.v_proj = torch.nn.Linear(embed_dim, embed_dim)
        self.q_proj = torch.nn.Linear(embed_dim, embed_dim)
        self.out_proj = torch.nn.Linear(embed_dim, embed_dim)
        self.attn_dropout = torch.nn.Dropout(dropout)
        self.softmax = torch.nn.Softmax(dim=-1)

    def forward(self, x1, x2):
        k = self.k_proj(x1)
        v = self.v_proj(x2)
        q = self.q_proj(x2)
        q = q.reshape(q.shape[0], q.shape[1], self.num_heads, q.shape[-1] // self.num_heads).transpose(2, 1)
        k = k.reshape(k.shape[0], k.shape[1], self.num_heads, k.shape[-1] // self.num_heads).transpose(2, 1)
        v = v.reshape(v.shape[0], v.shape[1], self.num_heads, v.shape[-1] // self.num_heads).transpose(2, 1)
        attn = q @ k.transpose(-2, -1) / math.sqrt(self.k_proj.weight.shape[-1])
        attn = attn + torch.ones_like(attn) * -100000.0
        attn = self.softmax(attn)
        attn = self.attn_dropout(attn)
        out = (attn @ v).transpose(2, 1).reshape(attn.shape[0], attn.shape[1], -1)
        out = self.out_proj(out)
        return out


embed_dim = 1
num_heads = 1
func = SelfAttention(256, 8).to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (192x64 and 256x256)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 3, 64, 64)), Parameter(FakeTensor(..., size=(256, 256), requires_grad=True)), Parameter(FakeTensor(..., size=(256,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [192, 64] X [256, 256].

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''