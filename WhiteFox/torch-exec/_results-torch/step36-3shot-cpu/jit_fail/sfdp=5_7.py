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

    def forward(self, query, key, value, attn_mask):
        qk = torch.softmax(query * key, 3)
        qk = qk + attn_mask
        attn_weight = torch.dropout(qk, 0.1, True)
        output = attn_weight * value
        return output



func = Model().to('cpu')


query = torch.randn(1, 160, 160, 256)

key = torch.randn(1, 160, 160, 256)

value = torch.randn(1, 160, 160, 256)

attn_mask = torch.randn(1, 1, 160, 160)

test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (256) must match the size of tensor b (160) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, s0, s1, s2)), FakeTensor(..., size=(1, 1, s6, s7))), **{}):
The size of tensor a (s2) must match the size of tensor b (s7) at non-singleton dimension 3)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''