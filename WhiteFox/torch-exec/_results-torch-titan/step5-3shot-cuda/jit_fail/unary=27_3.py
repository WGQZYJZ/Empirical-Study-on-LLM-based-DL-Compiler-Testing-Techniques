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
        self._linear1 = torch.nn.Linear(5, 1, bias=True)
        self._linear2 = torch.nn.Linear(2, 1, bias=True)

    def forward(self, x0):
        r0 = self._linear1(x0).reshape((- 1))
        r1 = torch.unsqueeze(r0, 1)
        v0 = torch.cat((r0, r1), 0)
        v1 = self._linear1(v0)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 1, 5, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x4 and 5x1)

jit:
Failed running call_module L__self____linear1(*(FakeTensor(..., device='cuda:0', size=(1, 1, 5, 4)),), **{}):
a and b must have same reduction dim, but got [5, 4] X [5, 1].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''