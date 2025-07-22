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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(64, 16, 2, stride=1, padding=0, bias=False)
        self.negative_slope = negative_slope
        self.conv_t_1 = torch.nn.ConvTranspose2d(16, 3, 3, stride=2, padding=0, bias=False)

    def forward(self, input0):
        y0 = input0.transpose((- 1), (- 3))
        y1 = self.conv_t(y0)
        y2 = (y1 > 0.0)
        y3 = (y1 * self.negative_slope)
        y4 = torch.where(y2, y1, y3)
        y5 = self.conv_t_1(y4)
        return y5



negative_slope = 1

func = Model(negative_slope).to('cuda')



input0 = torch.randn(16, 64, 12, 13)


test_inputs = [input0]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [64, 16, 2, 2], expected input[16, 13, 12, 64] to have 64 channels, but got 13 channels instead

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(16, 13, 12, 64)),), **{}):
Given transposed=1, weight of size [64, 16, 2, 2], expected input[16, 13, 12, 64] to have 64 channels, but got 13 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''