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

    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(100, 100)
        self.query = torch.nn.Linear(100, 100)
        self.dropout = torch.nn.Dropout(p=0.5)

    def forward(self, query, key):
        q = self.query(query)
        k = self.key(key)
        a = torch.matmul(q, k.transpose(-2, -1))
        s = a.div(10.0)
        m = s.softmax(dim=-1)
        d = self.dropout(m)
        o = torch.matmul(d, s)
        return o


func = Model().to('cpu')


query = torch.randn(1, 5, 100)

key = torch.randn(5, 100, 64, 64)

test_inputs = [query, key]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (32000x64 and 100x100)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(5, 100, 64, 64)), Parameter(FakeTensor(..., size=(100, 100), requires_grad=True)), Parameter(FakeTensor(..., size=(100,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [32000, 64] X [100, 100].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''