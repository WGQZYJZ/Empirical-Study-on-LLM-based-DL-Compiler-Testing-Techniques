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
        self.conv = torch.nn.Conv2d(10, 5, 1, stride=1, padding=0)

    def forward(self, x6):
        v1 = self.conv(x6)
        v2 = (v1 * 0.5)
        v3 = (v1 * v1)
        v4 = (v3 * v1)
        v5 = (v4 * 0.044715)
        v6 = (v1 + v5)
        v7 = (v6 * 0.7978845608028654)
        v8 = torch.tanh(v7)
        v9 = (v8 + 1)
        v10 = (v2 * v9)
        return v10




func = Model().to('cuda')



x6 = torch.randn(10, 5, 101, 169)


test_inputs = [x6]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [5, 10, 1, 1], expected input[10, 5, 101, 169] to have 10 channels, but got 5 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(10, 5, 101, 169)),), **{}):
Given groups=1, weight of size [5, 10, 1, 1], expected input[10, 5, 101, 169] to have 10 channels, but got 5 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''