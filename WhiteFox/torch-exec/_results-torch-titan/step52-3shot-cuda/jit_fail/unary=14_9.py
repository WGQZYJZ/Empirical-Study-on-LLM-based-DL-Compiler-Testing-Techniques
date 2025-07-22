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
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(16, 2, 7, stride=2, padding=3)
        self.conv_2 = torch.nn.Conv2d(12, 16, 7, stride=2, padding=3)
        self.conv_3 = torch.nn.Conv2d(16, 12, 7, stride=2, padding=3)

    def forward(self, x1):
        v1 = self.conv_transpose_2(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        v4 = self.conv_2(v3)
        v5 = torch.sigmoid(v4)
        v6 = (v4 * v5)
        v7 = self.conv_3(v6)
        v8 = torch.sigmoid(v7)
        v9 = (v7 * v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 2, 14, 14)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [16, 2, 7, 7], expected input[1, 2, 14, 14] to have 16 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv_transpose_2(*(FakeTensor(..., device='cuda:0', size=(1, 2, 14, 14)),), **{}):
Given transposed=1, weight of size [16, 2, 7, 7], expected input[1, 2, 14, 14] to have 16 channels, but got 2 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''