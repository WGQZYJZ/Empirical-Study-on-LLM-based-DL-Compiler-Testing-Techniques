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
        self.linear = torch.nn.Linear(8, 8)

    def forward(self, x, other):
        v1 = self.linear(x)
        v2 = (v1 + other)
        return v2



func = Model().to('cuda')



x = torch.randn(3, 32, 32)



other = torch.randn(4, 8)


test_inputs = [x, other]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (96x32 and 8x8)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(3, 32, 32)),), **{}):
a and b must have same reduction dim, but got [96, 32] X [8, 8].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''