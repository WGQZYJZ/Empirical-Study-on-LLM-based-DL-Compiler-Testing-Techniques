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

    def __init__(self, dim, n_heads):
        super().__init__()
        self.W_qkv = torch.nn.Linear(dim, 3 * dim)
        self.n_heads = n_heads

    def forward(self, query, key, value):
        qkv = self.W_qkv(query).reshape(query.shape[0], query.shape[1], 3, self.n_heads, self.dim)
        qkv = qkv.transpose(1, 2)
        q = qkv[0]
        k = qkv[1]
        v = qkv[2]
        scale_factor = torch.sqrt(torch.tensor(1 / (self.dim * self.n_heads)))
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.0, training=True)
        output = dropout_qk.matmul(v).transpose(1, 2)
        output = output.reshape(output.shape[0], output.shape[1], -1)
        return output


dim = 1
n_heads = 1

func = Model(dim, n_heads).to('cpu')


query = torch.randn(1, 8, 64)

key = torch.randn(1, 4, 64)

value = torch.randn(1, 4, 64)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x64 and 1x3)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 8, 64)), Parameter(FakeTensor(..., size=(3, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [8, 64] X [1, 3].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''