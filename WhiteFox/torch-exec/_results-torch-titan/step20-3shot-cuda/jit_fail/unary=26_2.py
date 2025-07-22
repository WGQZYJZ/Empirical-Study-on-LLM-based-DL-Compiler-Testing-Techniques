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

    def __init__(self, stride, padding, dilation):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(int((((480 * 7) / 8) + 0.5)), 7, 2, stride=stride, padding=padding, dilation=dilation)

    def forward(self, x1):
        x2 = self.conv_t(x1)
        x3 = x2
        x4 = (x3 > 0)
        x5 = (x3 * 0.5)
        x6 = torch.where(x4, x3, x5)
        return x6




stride = 2


padding = 1


dilation = 1


func = Model(stride, padding, dilation).to('cuda')



x1 = torch.randn(32, 480, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [420, 7, 2, 2], expected input[32, 480, 16, 16] to have 420 channels, but got 480 channels instead

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(32, 480, 16, 16)),), **{}):
Given transposed=1, weight of size [420, 7, 2, 2], expected input[32, 480, 16, 16] to have 420 channels, but got 480 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''