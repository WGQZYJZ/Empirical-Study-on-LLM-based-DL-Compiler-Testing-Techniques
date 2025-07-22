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
        self.linear = torch.nn.Linear(16, 2)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + t0)
        v3 = torch.nn.functional.relu(v2)
        return v3



func = Model().to('cuda')



t0 = torch.randn(2)


test_inputs = [t0]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2 and 16x2)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(2,)),), **{}):
a and b must have same reduction dim, but got [1, 2] X [16, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''