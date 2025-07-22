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
        self.conv = torch.nn.Conv2d(3, 16, 3, padding=(0, 1), dilation=(2, 3))

    def forward(self, x1):
        x2 = torch.randn(1, 3, 2, 3)
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv(x2)
        v4 = torch.sigmoid(v3)
        v5 = torch.randn(1, 3, 2, 3)
        v6 = self.conv(v5)
        v7 = torch.sigmoid(v6)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 5). Kernel size: (5 x 7). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., size=(1, 3, 2, 3)),), **{}):
Calculated padded input size per channel: (2 x 5). Kernel size: (5 x 7). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''