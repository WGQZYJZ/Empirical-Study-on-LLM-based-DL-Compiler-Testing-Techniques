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
        self.conv = torch.nn.Conv2d(2, 10, (5, 5), stride=(3, 3))

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sum(v1, dim=2)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 3, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (3 x 3). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3, 3)),), **{}):
Calculated padded input size per channel: (3 x 3). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''