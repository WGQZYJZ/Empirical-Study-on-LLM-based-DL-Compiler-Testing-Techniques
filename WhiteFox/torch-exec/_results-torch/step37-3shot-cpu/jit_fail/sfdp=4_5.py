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
        self.fc1 = torch.nn.Linear(2, 32)
        torch.nn.init.normal_(self.fc1.weight, std=0.01)
        self.fc2 = torch.nn.Linear(32, 64)

    def forward(self, Q0, K0, V0, mask):
        q = self.fc1(Q0)
        k = self.fc2(K0)
        v = self.fc1(V0)
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v
        return (output, qk)



func = Model().to('cpu')


Q = torch.randn(2, 2)

K = torch.randn(2, 2)

V = torch.randn(2, 2)

mask = (torch.rand(2, 2) > 0.7).fill_(-1000000000.0)

test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x2 and 32x64)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(2, 2)), Parameter(FakeTensor(..., size=(64, 32), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 2] X [32, 64].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''