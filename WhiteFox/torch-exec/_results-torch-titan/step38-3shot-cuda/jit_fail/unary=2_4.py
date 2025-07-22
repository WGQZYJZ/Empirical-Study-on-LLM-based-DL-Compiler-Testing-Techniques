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
        self.conv_1 = torch.nn.Conv2d(18, 20, 9, stride=2, padding=1)
        self.conv_2 = torch.nn.Conv2d(20, 16, 7, stride=3, padding=2)

    def forward(self, x1):
        v1 = self.conv_1(x1)
        v2 = self.conv_2(v1)
        v3 = (v1 + v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 18, 3, 9)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (5 x 11). Kernel size: (9 x 9). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv_1(*(FakeTensor(..., device='cuda:0', size=(1, 18, 3, 9)),), **{}):
Calculated padded input size per channel: (5 x 11). Kernel size: (9 x 9). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''