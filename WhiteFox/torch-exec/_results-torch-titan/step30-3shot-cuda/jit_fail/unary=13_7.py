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



class SigmoidGated(torch.nn.Module):

    def __init__(self, dim):
        super().__init__()
        self.dim = dim
        self.linear = torch.nn.Linear(self.dim, self.dim)

    def forward(self, x):
        t1 = self.linear(x)
        t2 = torch.sigmoid(t1)
        t3 = (t1 * t2)
        return t3




dim = 16

func = SigmoidGated(dim).to('cuda')



dim = 16


x = torch.randn(32, dim, 4, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2048x4 and 16x16)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(32, 16, 4, 4)),), **{}):
a and b must have same reduction dim, but got [2048, 4] X [16, 16].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''