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
        self.linear = torch.nn.Linear(640, 128)
        self.linear2 = torch.nn.Linear(128, 64)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 + x2
        v3 = self.linear2(v2)
        v4 = v3 + x1
        return v4


func = Model().to('cpu')


x1 = torch.randn(4, 640)

x2 = torch.randn(4, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (128) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0, 128)), FakeTensor(..., size=(4, 64))), **{}):
The size of tensor a (128) must match the size of tensor b (64) at non-singleton dimension 1)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''