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
        self.linear1 = torch.nn.Linear(32, 16, bias=False)
        self.linear2 = torch.nn.Linear(16, 8, bias=False)
        self.linear3 = torch.nn.Linear(32, 16, bias=False)
        self.linear4 = torch.nn.Linear(16, 8, bias=False)
        self.linear5 = torch.nn.Linear(32, 16, bias=False)
        self.linear6 = torch.nn.Linear(16, 8, bias=False)
        self.linear7 = torch.nn.Linear(28, 8, bias=False)

    def forward(self, q, k, v):
        q1 = self.linear1(q)
        q2 = self.linear2(q1)
        q3 = self.linear3(q)
        k1 = self.linear4(k)
        k2 = self.linear5(k1)
        k3 = self.linear6(k)
        k3.transpose_(-2, -1)
        attn_weight = torch.matmul(q2, k3)
        attn_weight = attn_weight / math.sqrt(q2.size(-1))
        mask = torch.triu(torch.ones(q1.size(0), k1.size(0)), diagonal=1) == 1
        attn_weight = attn_weight.masked_fill(mask, -math.inf)
        attn_weight = torch.softmax(attn_weight, dim=-1)
        output = torch.matmul(attn_weight, v)
        output.transpose_(-2, -1)
        tmp = torch.cat([output, q3], dim=-1)
        tmp.transpose_(-2, -1)
        o1 = self.linear7(tmp)
        o2 = self.linear7(output)
        return o1 + o2


func = Model().to('cpu')


q = torch.randn(32, 28)

k = torch.randn(32, 32)

v = torch.randn(32, 28)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (32x28 and 32x16)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(32, 28)), Parameter(FakeTensor(..., size=(16, 32), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [32, 28] X [32, 16].

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''