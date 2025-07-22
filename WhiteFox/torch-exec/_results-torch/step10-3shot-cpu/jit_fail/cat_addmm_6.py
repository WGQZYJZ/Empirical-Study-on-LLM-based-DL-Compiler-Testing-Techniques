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

    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2, x2)
        v2 = torch.cat([v1], dim=1)
        return v2


func = Model().to('cpu')


x1 = torch.randn(64, 512, requires_grad=True)

x2 = torch.randn(512, 512, requires_grad=True)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The expanded size of the tensor (512) must match the existing size (64) at non-singleton dimension 0.  Target sizes: [512, 512].  Tensor sizes: [64, 512]

jit:
Failed running call_function <built-in method addmm of type object at 0x71ddb4396ec0>(*(FakeTensor(..., size=(s2, s0)), FakeTensor(..., size=(s0, s0)), FakeTensor(..., size=(s0, s0))), **{}):
The size of tensor a (s0) must match the size of tensor b (s2) at non-singleton dimension 0)

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''