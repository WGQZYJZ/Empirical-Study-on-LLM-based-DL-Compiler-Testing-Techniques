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
        self.conv = torch.nn.Conv2d(3, 1, 1)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.bn(v1)
        v3 = self.conv(v2)
        v4 = torch.sigmoid(v3)
        return v4




func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 3, 1, 1], expected input[1, 1, 64, 64] to have 3 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 1, 64, 64)),), **{}):
Given groups=1, weight of size [1, 3, 1, 1], expected input[1, 1, 64, 64] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''