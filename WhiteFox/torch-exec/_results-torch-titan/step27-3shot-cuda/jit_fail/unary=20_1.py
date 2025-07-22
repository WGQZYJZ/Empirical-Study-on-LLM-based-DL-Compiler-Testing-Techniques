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



class Model_v2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(32, 16, 3, stride=2, groups=2)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(16, 8, 2, stride=2, dilation=1, groups=1)
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(8, 8, 2, stride=1, dilation=1, groups=1)

    def forward(self, x1):
        v0 = self.conv_transpose_1(x1)
        v1 = torch.sigmoid(v0)
        v2 = self.conv_transpose_2(v1)
        v3 = torch.tanh(v2)
        v4 = self.conv_transpose_3(v3)
        return v4



func = Model_v2().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___conv_transpose_1(*(1,), **{}):
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''