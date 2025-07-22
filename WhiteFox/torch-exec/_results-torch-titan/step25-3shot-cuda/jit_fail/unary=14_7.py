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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 3, stride=1, padding=1)
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(8, 8, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.conv_transpose_1(v1)
        v3 = torch.sigmoid(v2)
        v4 = (v2 * v3)
        v5 = self.conv_transpose(v4)
        v6 = self.conv_transpose_1(v3)
        v7 = torch.sigmoid(v4)
        v8 = (v4 * v7)
        v9 = (v5 + v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 3, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 8, 3, 3], expected input[1, 8, 16, 16] to have 3 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 8, 16, 16)),), **{}):
Given transposed=1, weight of size [3, 8, 3, 3], expected input[1, 8, 16, 16] to have 3 channels, but got 8 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''