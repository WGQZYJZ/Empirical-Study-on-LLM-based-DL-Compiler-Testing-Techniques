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
        self.linear = torch.nn.Linear(952, 336)

    def forward(self, x1):
        v1 = x1.flatten(1, (- 1))
        v2 = self.linear(v1)
        v3 = (torch.clamp(v2, max=6) + 3)
        v4 = (v3 * 0.16666666666666666)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 96, 88)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x8448 and 952x336)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 8448)),), **{}):
a and b must have same reduction dim, but got [1, 8448] X [952, 336].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''