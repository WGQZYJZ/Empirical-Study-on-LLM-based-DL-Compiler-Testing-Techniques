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
        self.linear = torch.nn.Linear(12, 8)

    def forward(self, x1):
        v5 = torch.add(x1, x1)
        v1 = self.linear(v5)
        v2 = torch.sigmoid(v1)
        v3 = torch.mm(v5, v5.t())
        v4 = v3 * v2
        return v4


func = Model().to('cpu')


x1 = torch.randn(5, 12)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(s0, s0)), FakeTensor(..., size=(s0, 8))), **{}):
The size of tensor a (s0) must match the size of tensor b (8) at non-singleton dimension 1)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''