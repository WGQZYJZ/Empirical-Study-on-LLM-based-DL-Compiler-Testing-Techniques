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

class MultiHeadAttentionLayer(torch.nn.Module):

    def __init__(self, embed_dim, num_heads=8, dropout=0.2, bias=True):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.dropout = dropout
        self.head_dim = embed_dim // num_heads
        self.scaling = self.head_dim ** (-0.5)
        self.wq = torch.nn.Linear(embed_dim, embed_dim, bias=bias)
        self.wk = torch.nn.Linear(embed_dim, embed_dim, bias=bias)
        self.wv = torch.nn.Linear(embed_dim, embed_dim, bias=bias)
        self.dense = torch.nn.Linear(embed_dim, embed_dim, bias=bias)

    def forward(self, inputs):
        v = self.wq(inputs)
        k = self.wk(inputs)
        q = self.wq(inputs)
        v = v.chunk(self.num_heads, dim=-1)
        k = k.chunk(self.num_heads, dim=-1)
        q = q.chunk(self.num_heads, dim=-1)
        return (v, k, q)

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.mhalayer = MultiHeadAttentionLayer(128)

    def forward(self, x1, x2, x3):
        (v, k, q) = self.mhalayer(x1)
        v = torch.stack(v)
        k = torch.stack(k)
        q = torch.stack(q)
        value_len = v.size()[-2]
        key_len = k.size()[-2]
        query_len = q.size()[-2]
        causal_mask = torch.triu(torch.ones(query_len, key_len), 1 + query_len - key_len).bool().to(x1.device)
        attn_mask = torch.tril(torch.ones(query_len, value_len, device=x1.device)).bool()
        attn_mask += causal_mask
        return (v, k, q, attn_mask)


func = Model().to('cpu')


x1 = torch.randn(24, 128, 8)

x2 = torch.randn(24, 128, 8)

x3 = torch.randn(24, 128, 8)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3072x8 and 128x128)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(24, 128, 8)), Parameter(FakeTensor(..., size=(128, 128), requires_grad=True)), Parameter(FakeTensor(..., size=(128,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [3072, 8] X [128, 128].

from user code:
   File "<string>", line 43, in forward
  File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''