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
        self.conv_t = torch.nn.ConvTranspose2d(4, 7, 2, stride=2)
        self.negative_slope = (- 0.1)

    def forward(self, x1):
        x2 = self.conv_t(x1)
        x3 = (x2 > 0)
        x4 = (x2 * self.negative_slope)
        x5 = torch.where(x3, x2, x4)
        return x5




func = Model().to('cuda')



x1 = torch.randn(16, 480, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [4, 7, 2, 2], expected input[16, 480, 16, 16] to have 4 channels, but got 480 channels instead

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(16, 480, 16, 16)),), **{}):
Given transposed=1, weight of size [4, 7, 2, 2], expected input[16, 480, 16, 16] to have 4 channels, but got 480 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''