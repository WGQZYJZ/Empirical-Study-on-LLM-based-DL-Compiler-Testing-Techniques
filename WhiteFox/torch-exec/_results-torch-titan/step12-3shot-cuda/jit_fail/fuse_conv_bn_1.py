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
        self.conv0 = torch.nn.Conv2d(4, 8, 3)
        self.bn0 = torch.nn.BatchNorm2d(8)
        self.conv1 = torch.nn.Conv2d(8, 16, 3)
        self.bn1 = torch.nn.BatchNorm2d(16)

    def forward(self, x3):
        x3 = self.bn0(self.conv0(x3))
        return self.bn1(self.conv1(x3))




func = Model().to('cuda')



x3 = torch.randn(1, 4, 4, 4)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 8, 2, 2)),), **{}):
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''