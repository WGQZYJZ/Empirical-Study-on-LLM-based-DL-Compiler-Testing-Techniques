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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(in_channels=2, out_channels=1, kernel_size=2, stride=2, padding=0)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(in_channels=2, out_channels=1, kernel_size=2, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv_transpose_2(x1)
        v2 = self.conv_transpose_1(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(2, 2, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [2, 1, 2, 2], expected input[2, 1, 128, 128] to have 2 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv_transpose_1(*(FakeTensor(..., device='cuda:0', size=(2, 1, 128, 128)),), **{}):
Given transposed=1, weight of size [2, 1, 2, 2], expected input[2, 1, 128, 128] to have 2 channels, but got 1 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''