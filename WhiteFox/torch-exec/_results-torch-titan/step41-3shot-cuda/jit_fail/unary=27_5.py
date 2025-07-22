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

    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv2d(64, 32, 3, padding=(- 1), dilation=1)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        return v3




min = (- 0.5)


max = 1


func = Model(min, max).to('cuda')



x1 = torch.randn(1, 64, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
negative padding is not supported

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 64, 4, 4)),), **{}):
negative padding is not supported

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''