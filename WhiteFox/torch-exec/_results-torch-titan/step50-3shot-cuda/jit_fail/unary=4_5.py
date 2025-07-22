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
        self.linear = torch.nn.Linear(29, 10)

    def forward(self, x1, x2):
        v1 = torch.cat((x1, x2), 1)
        v2 = self.linear(v1)
        v3 = (v2 * 0.5)
        v4 = (v2 * 0.7071067811865476)
        v5 = torch.erf(v4)
        v6 = (v5 + 1)
        v7 = (v3 * v6)
        return v7



func = Model().to('cuda')



x1 = torch.randn(1, 9)



x2 = torch.randn(1, 19)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x28 and 29x10)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 28)),), **{}):
a and b must have same reduction dim, but got [1, 28] X [29, 10].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''