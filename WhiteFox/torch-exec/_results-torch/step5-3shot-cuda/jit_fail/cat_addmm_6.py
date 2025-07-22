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

    def forward(self, x1, x5, x8):
        v1 = torch.addmm(x1, x5, x8)
        v2 = torch.cat([v1], 1)
        return v2


func = Model().to('cuda')


x1 = torch.randn(1, 14)

x5 = torch.randn(14, 256)

x8 = torch.randn(256, 256)

test_inputs = [x1, x5, x8]

# JIT_FAIL
'''
direct:
The expanded size of the tensor (256) must match the existing size (14) at non-singleton dimension 1.  Target sizes: [14, 256].  Tensor sizes: [1, 14]

jit:
Failed running call_function <built-in method addmm of type object at 0x7341f6f96ec0>(*(FakeTensor(..., device='cuda:0', size=(1, s0)), FakeTensor(..., device='cuda:0', size=(14, 256)), FakeTensor(..., device='cuda:0', size=(256, 256))), **{}):
The size of tensor a (256) must match the size of tensor b (s0) at non-singleton dimension 1)

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''