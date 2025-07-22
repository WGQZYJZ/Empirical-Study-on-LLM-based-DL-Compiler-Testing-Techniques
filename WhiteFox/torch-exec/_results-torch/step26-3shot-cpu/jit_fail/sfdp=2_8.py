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

    def __init__(self, dim, n_head, dropout_p=0.0):
        super().__init__()
        self.dim = dim
        self.n_head = n_head
        self.dropout_p = dropout_p
        self.linear_q = torch.nn.Linear(dim, dim)
        self.linear_k = torch.nn.Linear(dim, dim)
        self.linear_v = torch.nn.Linear(dim, dim)
        self.out_linear = torch.nn.Linear(dim, dim)

    def forward(self, query, key, value):
        bsz = query.size()[0]
        _query = query.repeat(self.n_head, 1, 1).view(self.n_head * bsz, -1, query.size(-1))
        _key = key.repeat(self.n_head, 1, 1).view(self.n_head * bsz, -1, key.size(-1))
        _value = value.repeat(self.n_head, 1, 1).view(self.n_head * bsz, -1, value.size(-1))
        q = self.linear_q(_query)
        k = self.linear_k(_key)
        v = self.linear_v(_value)
        inv_scale_factor = (self.dim // self.n_head) ** (-0.5)
        scaled_qk = torch.matmul(q, k.transpose(1, 2)) * inv_scale_factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = torch.matmul(dropout_qk, v)
        output = output.view(bsz, -1, self.n_head * self.dim)
        return self.out_linear(output)


dim = 1
n_head = 1
func = Model(256, 12, dropout_p=0.5).to('cpu')


query = torch.randn(3, 3, 256)

key = torch.randn(3, 5, 256)

value = torch.randn(3, 5, 256)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (9x3072 and 256x256)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(3, 3, 3072)), Parameter(FakeTensor(..., size=(256, 256), requires_grad=True)), Parameter(FakeTensor(..., size=(256,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [9, 3072] X [256, 256].

from user code:
   File "<string>", line 39, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''