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
        self.linear = torch.nn.Linear(16, 32)

    def forward(self, x1):
        flattened = torch.flatten(x1, 1)
        v1 = self.linear(flattened)
        v2 = torch.clamp_min(v1, min=0)
        v3 = torch.clamp_max(v2, max=255)
        reshape = v3.reshape(1, 16, 8, 8)
        sigmoid = torch.sigmoid(reshape)
        return sigmoid



func = Model().to('cuda')



x1 = torch.randn(1, 16, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x64 and 16x32)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 64)),), **{}):
a and b must have same reduction dim, but got [1, 64] X [16, 32].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''