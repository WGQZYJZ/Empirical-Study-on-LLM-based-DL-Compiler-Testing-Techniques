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
        self.conv1 = torch.nn.Conv2d(128, 512, 16, padding=0, stride=1)
        self.conv2 = torch.nn.Conv2d(512, 2, 3, padding=1, stride=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.tanh(v1)
        v3 = self.conv2(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 128, 1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 1). Kernel size: (16 x 16). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 128, 1, 1)),), **{}):
Calculated padded input size per channel: (1 x 1). Kernel size: (16 x 16). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''