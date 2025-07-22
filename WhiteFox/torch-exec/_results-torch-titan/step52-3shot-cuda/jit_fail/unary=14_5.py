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
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(4, 42, 6, stride=2, padding=2, dilation=1)
        self.conv_transpose_6 = torch.nn.ConvTranspose2d(140, 57, 7, stride=2, padding=3, dilation=1)
        self.conv_transpose_8 = torch.nn.ConvTranspose2d(57, 4, 7, stride=2, padding=3, dilation=1)

    def forward(self, x1):
        v1 = self.conv_transpose_3(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        v4 = self.conv_transpose_6(v3)
        v5 = torch.sigmoid(v4)
        v6 = (v4 * v5)
        v7 = self.conv_transpose_8(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 4, 15, 15)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [140, 57, 7, 7], expected input[1, 42, 30, 30] to have 140 channels, but got 42 channels instead

jit:
Failed running call_module L__self___conv_transpose_6(*(FakeTensor(..., device='cuda:0', size=(1, 42, 30, 30)),), **{}):
Given transposed=1, weight of size [140, 57, 7, 7], expected input[1, 42, 30, 30] to have 140 channels, but got 42 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''