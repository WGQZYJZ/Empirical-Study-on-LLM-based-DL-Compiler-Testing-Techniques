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

    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(1, 1, 1, bias=False)
        self.negative_slope = negative_slope

    def forward(self, x7):
        b4 = self.conv_t(x7)
        b5 = (b4 > 0)
        b6 = (b4 * self.negative_slope)
        b7 = torch.where(b5, b4, b6)
        return b7




func = Model().to('cuda')



x7 = torch.randn(1, 2, 7, 3)


test_inputs = [x7]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 1, 1, 1], expected input[1, 2, 7, 3] to have 1 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(1, 2, 7, 3)),), **{}):
Given transposed=1, weight of size [1, 1, 1, 1], expected input[1, 2, 7, 3] to have 1 channels, but got 2 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''