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
        _conv = torch.nn.Conv2d(3, 16, 1, stride=1, padding=2, bias=False)
        self.conv = torch.nn.Sequential(_conv, torch.nn.BatchNorm2d(16), torch.nn.ReLU(), _conv, torch.nn.BatchNorm2d(16), torch.nn.ReLU())

    def forward(self, x1):
        v1 = self.conv(x1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 3, 1, 1], expected input[1, 16, 36, 68] to have 3 channels, but got 16 channels instead

jit:
Failed running call_module L__self___conv_0(*(FakeTensor(..., device='cuda:0', size=(1, 16, 36, 68)),), **{}):
Given groups=1, weight of size [16, 3, 1, 1], expected input[1, 16, 36, 68] to have 3 channels, but got 16 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''