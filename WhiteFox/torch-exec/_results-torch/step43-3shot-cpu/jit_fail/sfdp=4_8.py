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

    def forward(self, Q4, k4, mask):
        qk = Q4 @ k4.transpose(-2, -1) / math.sqrt(Q4.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value



func = Model().to('cpu')


Q = torch.randn(1, 64, 256 + 64, 56)

K = torch.randn(1, 64, 256 + 64, 56)

mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)

test_inputs = [Q, K, mask]

# JIT_FAIL
'''
direct:
The size of tensor a (320) must match the size of tensor b (56) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 64, s1, 320)), FakeTensor(..., size=(1, 56, 56), dtype=torch.bool)), **{}):
The size of tensor a (320) must match the size of tensor b (56) at non-singleton dimension 3)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''