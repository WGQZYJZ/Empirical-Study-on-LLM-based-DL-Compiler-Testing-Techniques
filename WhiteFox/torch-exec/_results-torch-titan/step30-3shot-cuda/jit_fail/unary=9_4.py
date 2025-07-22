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
        self.conv = torch.nn.Conv2d(10, 8, 3, stride=3, padding=2, dilation=2)
        self.other_conv = torch.nn.Conv2d(8, 8, 97, stride=1, padding=97, dilation=97)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (2 + v1)
        v3 = v2.clamp(min=0, max=6)
        v4 = v3.div(6)
        v5 = self.other_conv(v4)
        v6 = (3 + v5)
        v7 = v6.clamp(min=0, max=6)
        v8 = (v7 / 6)
        return v8




func = Model().to('cuda')



x1 = torch.randn(5, 10, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (280 x 280). Kernel size: (9313 x 9313). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___other_conv(*(FakeTensor(..., device='cuda:0', size=(5, 8, 86, 86)),), **{}):
Calculated padded input size per channel: (280 x 280). Kernel size: (9313 x 9313). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''