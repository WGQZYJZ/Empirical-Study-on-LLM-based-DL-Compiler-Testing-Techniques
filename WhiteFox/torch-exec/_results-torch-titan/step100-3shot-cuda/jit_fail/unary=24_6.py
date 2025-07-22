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
        self.conv = torch.nn.Conv2d(4, 10, (7, 8), stride=(1, 3), padding=(3, 2))

    def forward(self, x):
        negative_slope = (- 0.767292)
        v1 = self.conv(x)
        v2 = (v1 > 0)
        v3 = (v1 * negative_slope)
        v4 = torch.where(v2, v1, v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 4, 19, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (25 x 5). Kernel size: (7 x 8). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 4, 19, 1)),), **{}):
Calculated padded input size per channel: (25 x 5). Kernel size: (7 x 8). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''