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

    def forward(self, q1, k2, v3):
        v1 = torch.matmul(q1, k2.transpose(-2, -1))
        v2 = v1 * 1.0 / v1.shape[-1] ** 0.5
        v4 = torch.nn.functional.softmax(v2, dim=-1)
        v5 = torch.nn.functional.dropout(v4, p=0.9)
        v6 = torch.matmul(v5, v3)
        return v6


func = Model().to('cpu')


q1 = torch.randn(1, 3, 64, 64)

k2 = torch.randn(1, 4, 64, 64)

v3 = torch.randn(1, 4, 64, 64)

test_inputs = [q1, k2, v3]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7751bd996ec0>(*(FakeTensor(..., size=(1, 3, 64, 64)), FakeTensor(..., size=(1, 4, 64, 64))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''