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
        self.linear = torch.nn.Linear(64, 64)

    def forward(self, x1, other=None):
        if (other is None):
            other = torch.rand_like(x1, dtype=x1.dtype)
        if (not torch.is_tensor(other)):
            raise TypeError(('other must be a Torch tensor; but other.dtype == %s' % other.dtype))
        v1 = self.linear(x1)
        v2 = (v1 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 64, 8, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (512x8 and 64x64)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 64, 8, 8)),), **{}):
a and b must have same reduction dim, but got [512, 8] X [64, 64].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''