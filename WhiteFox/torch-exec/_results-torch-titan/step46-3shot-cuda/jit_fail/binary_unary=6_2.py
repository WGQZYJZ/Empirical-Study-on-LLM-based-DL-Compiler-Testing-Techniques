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
        self.linear = torch.nn.Linear((8 * 8), (32 * 32))

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 - 1.0)
        v3 = (v1 - 1.5)
        v4 = (v1 - 2.0)
        v5 = (v1 - 2.5)
        v6 = (v1 - 3.0)
        v7 = torch.max(v2, v3)
        v8 = torch.max(v4, v5)
        v9 = torch.max(v6, v7)
        v10 = torch.max(v6, v8)
        v11 = torch.max(v9, v10)
        v12 = torch.max(v9, v11)
        v13 = torch.max(v12, v11)
        v14 = torch.max(v12, v13)
        return v14



func = Model().to('cuda')



x1 = torch.randn(1, 2, 8, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x8 and 64x1024)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 2, 8, 8)),), **{}):
a and b must have same reduction dim, but got [16, 8] X [64, 1024].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''