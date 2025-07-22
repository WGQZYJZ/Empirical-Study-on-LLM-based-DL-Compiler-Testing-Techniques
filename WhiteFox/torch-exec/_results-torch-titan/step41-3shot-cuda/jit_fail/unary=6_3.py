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
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1, dilation=1)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = (3 + t1)
        t3 = t2.clamp(0, 6)
        t4 = (t1 * t3)
        t5 = t4
        w = tuple((1 for _ in range(t5.dim())))
        s = tuple((2 for _ in range(t5.dim())))
        t7 = F.avg_pool2d(t5.contiguous(), kernel_size=1, stride=2, padding=0, ceil_mode=False, count_include_pad=True)
        t8 = t7.contiguous().view(t7.size(0), (- 1))
        t9 = self.bn(t8)
        return t9




func = Model().to('cuda')



x1 = torch.randn(2, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected 4D input (got 2D input)

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(2, 3267)),), **{}):
expected 4D input (got 2D input)

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''