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
        self.linear = torch.nn.Linear(((64 * 64) * 3), 1)
        self.other = torch.nn.Parameter(torch.randn(1))

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + self.other)
        v3 = relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(8, 64, 64, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (32768x3 and 12288x1)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(8, 64, 64, 3)),), **{}):
a and b must have same reduction dim, but got [32768, 3] X [12288, 1].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''