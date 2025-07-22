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

    def __init__(self, i):
        super().__init__()
        self.linear = torch.nn.Linear(i, 1)

    def forward(self, x2, x3, x4):
        v0 = torch.add(x3, x4)
        v1 = self.linear(x2)
        v8 = torch.add(v1, v0)
        return v8



i = 1

func = Model(i).to('cuda')



x2 = torch.randn(1, 100)



x3 = torch.randn(1, 100)



x4 = torch.randn(1, 100)


test_inputs = [x2, x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x100 and 1x1)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 100)),), **{}):
a and b must have same reduction dim, but got [1, 100] X [1, 1].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''