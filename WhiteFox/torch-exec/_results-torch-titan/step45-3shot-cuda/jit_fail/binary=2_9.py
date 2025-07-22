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
        self.conv = torch.nn.Conv2d(4, 64, 5, stride=3, padding=0, dilation=1, groups=1, bias=False)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 - 0)
        return v2




func = Model().to('cuda')



x = torch.randn(1, 8, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 4, 5, 5], expected input[1, 8, 64, 64] to have 4 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)),), **{}):
Given groups=1, weight of size [64, 4, 5, 5], expected input[1, 8, 64, 64] to have 4 channels, but got 8 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''