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
        self.conv = torch.nn.Conv2d(2, 2, 1, stride=1, padding=0, dilation=2, groups=2)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.sigmoid(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 5, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=2, weight of size [2, 1, 1, 1], expected input[1, 5, 64, 64] to have 2 channels, but got 5 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 5, 64, 64)),), **{}):
Given groups=2, weight of size [2, 1, 1, 1], expected input[1, 5, 64, 64] to have 2 channels, but got 5 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''