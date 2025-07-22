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
        self.linear = torch.nn.Linear(23, 2)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = self.linear(v1)
        v3 = torch.cat([v1, v2], dim=1)
        v4 = (v3 + 3)
        v5 = torch.clamp_min(v4, 0)
        v6 = torch.clamp_max(v5, 6)
        v7 = (v6 / 6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 23)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2 and 23x2)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 2)),), **{}):
a and b must have same reduction dim, but got [1, 2] X [23, 2].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''