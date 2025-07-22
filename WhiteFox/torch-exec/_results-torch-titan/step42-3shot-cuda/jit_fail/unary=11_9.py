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
        self.conv_transpose = torch.nn.ConvTranspose2d(2, 2, 5, stride=3, padding=1)
        self.avg_pool2d = torch.nn.AvgPool2d(2, stride=2, padding=5)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 + 3)
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = (v4 / 6)
        v6 = self.avg_pool2d(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 2, 30, 30)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of kernel size, but got pad=5 and kernel_size=2

jit:
Failed running call_module L__self___avg_pool2d(*(FakeTensor(..., device='cuda:0', size=(1, 2, 90, 90)),), **{}):
pad should be at most half of kernel size, but got pad=5 and kernel_size=2

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''