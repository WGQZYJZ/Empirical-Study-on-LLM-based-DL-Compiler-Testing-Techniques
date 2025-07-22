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

    def __init__(self, dim, num_heads, dropout):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.dropout = dropout
        self.q_proj = torch.nn.Linear(dim, dim)
        self.k_proj = torch.nn.Linear(dim, dim)
        self.v_proj = torch.nn.Linear(dim, dim)
        self.out_dropout = torch.nn.Dropout(dropout)

    def forward(self, query, key):
        scale_factor = 1.0 / math.sqrt(self.dim)
        q = self.q_proj(query)
        k = self.k_proj(key)
        v = self.v_proj(key)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout)
        return self.out_dropout(dropout_qk.matmul(v))


dim = 1
num_heads = 1
dropout = 1

func = Model(dim, num_heads, dropout).to('cpu')


query = torch.randn(1, 8, 128)

key = torch.randn(1, 8, 128)

test_inputs = [query, key]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x128 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 8, 128)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [8, 128] X [1, 1].

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''