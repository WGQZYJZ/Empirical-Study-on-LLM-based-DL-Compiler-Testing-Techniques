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

    def forward(self, q, k, v, mask):
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        qk = qk + mask
        attn_weight = torch.matmul(qk, v)
        attn_weight.masked_fill_(mask == 0.0, -1000000000.0)
        attn_weight = torch.softmax(attn_weight.float(), dim=-1)
        attn_weight = attn_weight.type_as(q)
        output = attn_weight @ v
        return output



func = Model().to('cpu')


Q = torch.randn(1, 32, 9, 9)

K = torch.randn(1, 32, 9, 9)

V = torch.randn(1, 32, 9, 9)


mask = (torch.rand(1, 9, 9, 9) > 0.7).fill_(float('-inf'))

test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (9) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, s0, s4, s1)), FakeTensor(..., size=(1, s6, s4, s1), dtype=torch.bool)), **{}):
The size of tensor a (s0) must match the size of tensor b (s6) at non-singleton dimension 1)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''