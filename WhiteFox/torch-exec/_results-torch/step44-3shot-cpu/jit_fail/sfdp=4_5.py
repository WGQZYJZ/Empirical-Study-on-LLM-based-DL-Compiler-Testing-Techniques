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

    def forward(self, x, k2, v2, mask):
        qk = x.transpose(-2, -1) @ k2 / math.sqrt(x.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v2
        return output



func = Model().to('cpu')


Q = torch.randn(1, 56, 56, 64)

K = torch.randn(1, 56, 56, 64)

V = torch.randn(1, 56, 56, 64)

mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)

test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (56) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, s0, s1, s3)), FakeTensor(..., size=(1, 56, 56), dtype=torch.bool)), **{}):
The size of tensor a (s3) must match the size of tensor b (56) at non-singleton dimension 3)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''