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

    def forward(self, Q, K, V, mask):
        qk = Q @ K.transpose(-2, -1) / math.sqrt(Q.size(-1))
        qk = qk.permute(0, 2, 3, 1)
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ V
        return output



func = Model().to('cpu')


Q = torch.randn(1, 1024, 56, 56)

K = torch.randn(1, 1024, 56, 56)

V = torch.randn(1, 1024, 56, 56)

mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)

test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
The size of tensor a (1024) must match the size of tensor b (56) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 56, 56, s0)), FakeTensor(..., size=(1, 56, 56), dtype=torch.bool)), **{}):
The size of tensor a (s0) must match the size of tensor b (56) at non-singleton dimension 3)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''