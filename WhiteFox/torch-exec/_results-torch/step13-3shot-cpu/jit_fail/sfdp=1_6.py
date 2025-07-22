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

    def __init__(self, num_heads, qkv_dim, dropout_p):
        super().__init__()
        self.qkv = torch.nn.Linear(qkv_dim, qkv_dim * 3)
        self.num_heads = num_heads
        self.dropout_p = dropout_p

    def forward(self, qkv):
        qkv = self.qkv(qkv)
        (query, key, value) = torch.chunk(qkv, 3, dim=-1)
        num_qkv = query.shape[-2]
        inv_scale_factor = 1.0 / self.num_heads ** 0.5
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)).div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output


num_heads = 1
qkv_dim = 1
dropout_p = 1

func = Model(num_heads, qkv_dim, dropout_p).to('cpu')


x1 = torch.randn(1, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (64x64 and 1x3)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 64, 64)), Parameter(FakeTensor(..., size=(3, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [64, 64] X [1, 3].

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''