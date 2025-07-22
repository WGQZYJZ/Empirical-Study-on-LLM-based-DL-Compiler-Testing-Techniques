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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2, x3):
        v1 = self.conv(x1)
        v2 = torch.matmul(v1, x2.transpose(-2, -1))
        v3 = v2.div(0.5)
        v4 = v2.softmax(dim=-1)
        v5 = torch.nn.functional.dropout(v4, p=0.25)
        v6 = v3 * v5
        m = torch.matmul(v6, x3)
        return m


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 32, 64, 64)

x3 = torch.randn(1, 5, 64, 64)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (32) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7842b6196ec0>(*(FakeTensor(..., size=(1, 8, s1 + 2, s2 + 2)), FakeTensor(..., size=(1, 32, 64, 64))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''