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
        self.linear = torch.nn.Linear(16, 16, bias=False)
        self.other = Parameter(torch.randn(16, 1, 4, 4))

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 - self.other)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 16, 5, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (80x5 and 16x16)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 16, 5, 5)),), **{}):
a and b must have same reduction dim, but got [80, 5] X [16, 16].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''