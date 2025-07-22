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
        self.conv = torch.nn.Conv2d(3, 64, 1, stride=1, padding=0, dilation=1)
        self.flatten = torch.flatten
        self.linear = torch.nn.Linear(((64 * 3) * 3), 3)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.flatten(v1)
        v3 = self.linear(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x262144 and 576x3)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(262144,)),), **{}):
a and b must have same reduction dim, but got [1, 262144] X [576, 3].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''