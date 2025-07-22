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

    def __init__(self, dim, num_heads, dropout_rate):
        super().__init__()
        self.query = torch.nn.Linear(dim, dim)
        self.key = torch.nn.Linear(dim, dim)
        self.value = torch.nn.Linear(dim, dim)
        self.dropout = torch.nn.Dropout(p=dropout_rate)

    def forward(self, query, key, value, mask):
        q = self.query(query)
        k = self.key(key)
        v = self.value(value)
        scaled_qk = torch.matmul(q, k.transpose(-2, -1))
        inv_scale_factor = 1.0 / np.sqrt(q.shape[-1])
        softmax_qk = scaled_qk.div(inv_scale_factor).softmax(dim=-1)
        tmp = softmax_qk.div(self.dropout(softmax_qk))
        output = torch.matmul(tmp, v)
        return output


dim = 1
num_heads = 1
dropout_rate = 1

func = Model(dim, num_heads, dropout_rate).to('cpu')


query = torch.randn(1, 2, 2)

key = torch.randn(1, 2, 2)

value = torch.randn(1, 2, 2)
mask = 1

test_inputs = [query, key, value, mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x2 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 2)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 2] X [1, 1].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''