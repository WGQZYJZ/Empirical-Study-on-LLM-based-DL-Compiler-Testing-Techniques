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
        self.conv_transpose_0 = torch.nn.ConvTranspose2d(1593, 44, 1, stride=1, padding=0)
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(2528, 39128, 1, stride=1, padding=0)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(44, 2528, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv_transpose_0(x1)
        v2 = torch.sigmoid(v1)
        v4 = self.conv_transpose_1(x1)
        v5 = torch.sigmoid(v4)
        v6 = (v4 * v5)
        v7 = torch.cat([v2, v6], dim=1)
        v7 = torch.flatten(v7)
        v8 = self.conv_transpose_2(v7.reshape([7, 4364, 5, 5]))
        v9 = torch.sigmoid(v8)
        v10 = (v8 * v9)
        return v10




func = Model().to('cuda')



x1 = torch.randn(1, 1593, 41, 41)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [2528, 39128, 1, 1], expected input[1, 1593, 41, 41] to have 2528 channels, but got 1593 channels instead

jit:
Failed running call_module L__self___conv_transpose_1(*(FakeTensor(..., device='cuda:0', size=(1, 1593, 41, 41)),), **{}):
Given transposed=1, weight of size [2528, 39128, 1, 1], expected input[1, 1593, 41, 41] to have 2528 channels, but got 1593 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''