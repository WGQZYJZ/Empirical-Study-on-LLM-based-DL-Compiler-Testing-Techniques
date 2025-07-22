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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 1, 3, stride=1, padding=1)
        self.avg_pool2d = torch.nn.AvgPool2d(1, stride=1, padding=1, count_include_pad=True)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.avg_pool2d(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of kernel size, but got pad=1 and kernel_size=1

jit:
Failed running call_module L__self___avg_pool2d(*(FakeTensor(..., device='cuda:0', size=(1, 1, 2, 2)),), **{}):
pad should be at most half of kernel size, but got pad=1 and kernel_size=1

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''