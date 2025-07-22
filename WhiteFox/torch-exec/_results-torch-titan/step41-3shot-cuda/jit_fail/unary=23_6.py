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
        self.avg_pool = torch.nn.AvgPool2d(kernel_size=2, stride=1, padding=0)
        self.avg_pool_1 = torch.nn.AvgPool2d(kernel_size=1, stride=1, padding=1)
        self.avg_pool_2 = torch.nn.AvgPool2d(kernel_size=1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.avg_pool(x1)
        v2 = self.avg_pool_1(v1)
        v3 = self.avg_pool_2(v1)
        v4 = torch.tanh(v2)
        v5 = torch.mul(v2, v3)
        v6 = torch.add(v4, v5)
        v7 = torch.mul(x1, v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 3, 18, 18)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of kernel size, but got pad=1 and kernel_size=1

jit:
Failed running call_module L__self___avg_pool_1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 17, 17)),), **{}):
pad should be at most half of kernel size, but got pad=1 and kernel_size=1

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''