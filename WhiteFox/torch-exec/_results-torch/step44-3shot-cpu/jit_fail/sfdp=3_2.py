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

    def __init__(self, seq_len, heads, ff_dim, dropout, scale_factor):
        super().__init__()
        self.query = torch.nn.Linear(seq_len, ff_dim)
        self.key = torch.nn.Linear(seq_len, ff_dim)
        self.value = torch.nn.Linear(seq_len, ff_dim)
        self.dropout_p = dropout
        self.scale_factor = scale_factor

    def forward(self, sequence):
        q = self.query(sequence)
        v = self.value(sequence)
        k = self.key(sequence)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        return output


seq_len = 1
heads = 1
ff_dim = 1
dropout = 1
scale_factor = 1

func = Model(seq_len, heads, ff_dim, dropout, scale_factor).to('cpu')


x1 = torch.randn(1, 16, 300)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x300 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 16, 300)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [16, 300] X [1, 1].

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''