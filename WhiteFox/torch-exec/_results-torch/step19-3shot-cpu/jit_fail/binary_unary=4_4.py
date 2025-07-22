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
        self.linear = torch.nn.Linear(200, 200)

    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.nn.ReLU()(v2)
        return v3


func = Model().to('cpu')


other = torch.rand(200, 200)

x1 = torch.randn(100, 200)

test_inputs = [other, x1]

# JIT_FAIL
'''
direct:
The size of tensor a (200) must match the size of tensor b (100) at non-singleton dimension 0

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0, 200)), FakeTensor(..., size=(s2, 200))), **{}):
The size of tensor a (s0) must match the size of tensor b (s2) at non-singleton dimension 0)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''