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
        self.linear = torch.nn.Linear(64, 32)

    def forward(self, x2, x3):
        v1 = self.linear(x3)
        v2 = v1 + x2
        return v2


func = Model().to('cpu')


x2 = torch.randn(1, 64)

x3 = torch.randn(1, 64)

test_inputs = [x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 32)), FakeTensor(..., size=(1, s0))), **{}):
The size of tensor a (32) must match the size of tensor b (s0) at non-singleton dimension 1)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''