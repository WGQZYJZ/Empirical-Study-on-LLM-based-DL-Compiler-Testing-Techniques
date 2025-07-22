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

    def forward(self, x2, v1, k, v2, v4, mask):
        qk = x2 @ k.transpose(-2, -1) / math.sqrt(x2.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ (v1 + (v2 - v2.mean()) + (v4 - v4.mean()))
        return output



func = Model().to('cpu')


Q = torch.randn(1, 64, 56, 56)

K = torch.randn(1, 64, 56, 56)

V = torch.randn(1, 64, 56, 56)

mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
x2 = 1
v1 = 1

test_inputs = [Q, K, V, mask, x2, v1]

# JIT_FAIL
'''
direct:
mean(): could not infer output dtype. Input dtype must be either a floating point or complex dtype. Got: Bool

jit:
Failed running call_method mean(*(FakeTensor(..., size=(1, 56, 56), dtype=torch.bool),), **{}):
mean(): could not infer output dtype. Input dtype must be either a floating point or complex dtype. Got: torch.bool

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''