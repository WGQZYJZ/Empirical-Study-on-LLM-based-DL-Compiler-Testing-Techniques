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

    def forward(self, query, key, value, scale_factor, dropout_p):
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1.mul(scale_factor)
        v3 = torch.nn.functional.softmax(v2, dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        v5 = torch.matmul(v4, value)
        return v5


func = Model().to('cpu')


query = torch.randn(2, 3, 4, 5)

key = torch.randn(2, 4, 5, 6)

value = torch.randn(2, 4, 5, 6)
scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7665fad96ec0>(*(FakeTensor(..., size=(s4, s5, s6, s7)), FakeTensor(..., size=(s0, s1, s3, s2))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''