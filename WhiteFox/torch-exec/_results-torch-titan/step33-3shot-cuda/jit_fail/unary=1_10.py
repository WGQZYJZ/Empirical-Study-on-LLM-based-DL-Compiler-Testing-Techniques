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
        self.linear = torch.nn.Linear(64, 16)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 + (((v1 * v1) * v1) * 0.044715))
        v4 = (v3 * 0.7978845608028654)
        v5 = torch.tanh(v4)
        v6 = (v5 + 1)
        v7 = (v2 * v6)
        return v7



func = Model().to('cuda')



x1 = torch.randn(1, 64, 3, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (192x5 and 64x16)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 64, 3, 5)),), **{}):
a and b must have same reduction dim, but got [192, 5] X [64, 16].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''