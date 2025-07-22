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
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 3)
        self.linear3 = torch.nn.Linear(8, 1)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = (v1 + 3)
        v3 = torch.max(torch.min(v2, torch.tensor(6.0)), torch.tensor(0.0))
        v4 = (v3 / 6)
        v5 = self.linear2(v4)
        v6 = self.linear3(v5)
        return v6



func = Model().to('cuda')



__x1__ = torch.randn(1, 3)


test_inputs = [__x1__]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x3 and 8x1)

jit:
Failed running call_module L__self___linear3(*(FakeTensor(..., device='cuda:0', size=(1, 3)),), **{}):
a and b must have same reduction dim, but got [1, 3] X [8, 1].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''