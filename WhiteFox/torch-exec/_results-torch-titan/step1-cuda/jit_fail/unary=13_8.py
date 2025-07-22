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
        self.linear1 = torch.nn.Linear(8, 16)
        self.linear2 = torch.nn.Linear(16, 16)

    def forward(self, x, h1, h2):
        v1 = self.linear1(x)
        v2 = (v1 * v2)
        return v2



func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)



h1 = torch.randn(1, 16)



h2 = torch.randn(1, 16)


test_inputs = [x, h1, h2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (192x64 and 8x16)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
a and b must have same reduction dim, but got [192, 64] X [8, 16].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''