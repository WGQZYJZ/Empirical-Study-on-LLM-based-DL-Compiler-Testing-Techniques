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
        self.linear1 = torch.nn.Linear(2, 4)

    def forward(self, x1):
        v1 = x1.mean(dim=1, keepdim=True)
        v2 = self.linear1(v1)
        v3 = ((v2 * torch.clamp(v2, 0, 6)) + 3)
        v4 = (v3 / 6)
        return v4



func = Model().to('cuda')



x1 = torch.randn(2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x1 and 2x4)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(2, 1)),), **{}):
a and b must have same reduction dim, but got [2, 1] X [2, 4].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''