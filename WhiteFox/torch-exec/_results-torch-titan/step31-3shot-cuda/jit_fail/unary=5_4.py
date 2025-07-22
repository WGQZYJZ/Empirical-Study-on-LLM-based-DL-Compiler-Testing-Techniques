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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(4, 64, 8, stride=8, padding=4)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(1, 32, 8, stride=1, padding=8)

    def forward(self, x1):
        t1 = self.conv_transpose_2(self.conv_transpose_1(x1))
        v1 = (t1 * 0.5)
        v2 = (t1 * 0.7071067811865476)
        v3 = torch.erf(v2)
        v4 = (v3 + 1)
        v5 = (v1 * v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 1, 255, 80)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [4, 64, 8, 8], expected input[1, 1, 255, 80] to have 4 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv_transpose_1(*(FakeTensor(..., device='cuda:0', size=(1, 1, 255, 80)),), **{}):
Given transposed=1, weight of size [4, 64, 8, 8], expected input[1, 1, 255, 80] to have 4 channels, but got 1 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''