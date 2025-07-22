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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(512, 704, 2, stride=2, padding=(1, 1), dilation=1)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(704, 272, 2, stride=2, padding=(1, 1), dilation=1)
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(272, 16, 2, stride=2, padding=(1, 1), dilation=1)
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(16, 72, 7, stride=1, padding=(3, 3), dilation=(3, 3))
        self.conv_transpose_5 = torch.nn.ConvTranspose2d(72, 16, 14, stride=1, padding=(6, 6), dilation=(6, 6))
        self.conv_transpose_6 = torch.nn.ConvTranspose2d(16, 2, 28, stride=1, padding=(12, 12), dilation=(12, 12))
        self.conv_transpose_7 = torch.nn.ConvTranspose2d(2, 4, 56, stride=1, padding=(24, 24), dilation=(24, 24))

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = self.conv_transpose_2(v1)
        v3 = self.conv_transpose_3(v2)
        v4 = self.conv_transpose_4(v3)
        v5 = self.conv_transpose_5(v3)
        v6 = self.conv_transpose_6(v5)
        v7 = self.conv_transpose_7(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 512, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [72, 16, 14, 14], expected input[1, 16, 498, 498] to have 72 channels, but got 16 channels instead

jit:
Failed running call_module L__self___conv_transpose_5(*(FakeTensor(..., device='cuda:0', size=(1, 16, 498, 498)),), **{}):
Given transposed=1, weight of size [72, 16, 14, 14], expected input[1, 16, 498, 498] to have 72 channels, but got 16 channels instead

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''