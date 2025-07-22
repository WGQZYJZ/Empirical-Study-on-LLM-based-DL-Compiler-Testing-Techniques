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
        self.linear = torch.nn.Linear(2, 8)
        self.negative_slope = 0.35

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = (v1 > 0)
        v3 = (v1 * self.negative_slope)
        v4 = torch.where(v2, v1, v3)
        v5 = self.linear(x2)
        v6 = (v5 > 0)
        v7 = (v5 * self.negative_slope)
        v8 = torch.where(v6, v5, v7)
        return torch.cat([v4, v8])



func = Model().to('cuda')



x1 = torch.randn(1, 2, 8)



x2 = torch.randn(1, 2, 8)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x8 and 2x8)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 2, 8)),), **{}):
a and b must have same reduction dim, but got [2, 8] X [2, 8].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''