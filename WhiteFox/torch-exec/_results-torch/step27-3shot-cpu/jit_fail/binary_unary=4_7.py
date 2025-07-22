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
        self.linear = torch.nn.Linear(32, 8)

    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = F.relu(v2)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 32)

x1 = torch.randn(1, 32)
other = torch.randn_like(x1)

test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (32) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8)), FakeTensor(..., size=(1, s1))), **{}):
The size of tensor a (8) must match the size of tensor b (s1) at non-singleton dimension 1)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''