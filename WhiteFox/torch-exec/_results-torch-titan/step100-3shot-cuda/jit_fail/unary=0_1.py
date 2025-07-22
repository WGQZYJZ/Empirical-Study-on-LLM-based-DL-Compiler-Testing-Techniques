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
        self.avg_pool = torch.nn.AvgPool2d((3, 3), stride=1, padding=2, ceil_mode=False, count_include_pad=True)
        self.conv1 = torch.nn.Conv2d(16, 44, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(44, 43, 1, stride=1, padding=0)

    def forward(self, x7293):
        v1 = self.avg_pool(x7293)
        v2 = self.conv1(v1)
        v3 = (v2 * 0.5)
        v4 = (v2 * v2)
        v5 = (v4 * v2)
        v6 = (v5 * 0.044715)
        v7 = (v2 + v6)
        v8 = (v7 * 0.7978845608028654)
        v9 = torch.tanh(v8)
        v10 = (v9 + 1)
        v11 = (v3 * v10)
        v12 = self.conv2(v11)
        return v12




func = Model().to('cuda')



x7293 = torch.randn(1, 16, 57, 15)


test_inputs = [x7293]

# JIT_FAIL
'''
direct:
pad should be at most half of kernel size, but got pad=2 and kernel_size=3

jit:
Failed running call_module L__self___avg_pool(*(FakeTensor(..., device='cuda:0', size=(1, 16, 57, 15)),), **{}):
pad should be at most half of kernel size, but got pad=2 and kernel_size=3

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''