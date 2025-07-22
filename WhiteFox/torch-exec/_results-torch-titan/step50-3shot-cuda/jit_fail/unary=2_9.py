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
        self.conv2d = torch.nn.Conv2d(33, 83, 8, stride=2, padding=2, groups=1, bias=True, dilation=1)
        self.batch_norm2d = torch.nn.BatchNorm2d(142, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.tanh = torch.nn.Tanh()

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = self.batch_norm2d(v1)
        v3 = self.tanh(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 33, 51, 91)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 83 elements not 142

jit:
Failed running call_module L__self___batch_norm2d(*(FakeTensor(..., device='cuda:0', size=(1, 83, 24, 44)),), **{}):
running_mean should contain 83 elements not 142

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''