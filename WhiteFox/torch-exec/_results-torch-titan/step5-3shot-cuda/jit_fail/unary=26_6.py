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
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 3, stride=2, padding=1, output_padding=1)
        self.negative_slope = negative_slope
        self.conv = torch.nn.Conv2d(1, 1, 1, stride=1, padding=0)

    def forward(self, x1):
        x2 = self.conv(x1)
        x3 = (x2 > 0)
        x4 = (x2 * self.negative_slope)
        x5 = torch.where(x3, x2, x4)
        return x5




negative_slope = 1


func = Model(negative_slope).to('cuda')



x1 = torch.randn(1, 8, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 8, 64, 64] to have 1 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)),), **{}):
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 8, 64, 64] to have 1 channels, but got 8 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''