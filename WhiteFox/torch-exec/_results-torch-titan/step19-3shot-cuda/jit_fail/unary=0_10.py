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
        self.conv = torch.nn.Conv2d(10, 5, 3, stride=3, padding=2)
        self.conv2 = torch.nn.Conv2d(1, 1, 1, stride=1, padding=0)

    def forward(self, x1, x2):
        x3 = torch.cat([x1, x2], 1)
        x4 = self.conv(x3)
        x5 = (x4 * 0.5)
        x6 = (x4 * x4)
        x7 = (x6 * x4)
        x8 = (x7 * 0.044715)
        x9 = (x5 + x7)
        x10 = (x9 * 0.7978845608028654)
        x11 = torch.tanh(x8)
        v10 = (x11 + 1)
        x13 = (x10 * v10)
        return x13




func = Model().to('cuda')



x1 = torch.randn(1, 10, 384, 46)



x2 = torch.randn(1, 1, 384, 46)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [5, 10, 3, 3], expected input[1, 11, 384, 46] to have 10 channels, but got 11 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 11, 384, 46)),), **{}):
Given groups=1, weight of size [5, 10, 3, 3], expected input[1, 11, 384, 46] to have 10 channels, but got 11 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''