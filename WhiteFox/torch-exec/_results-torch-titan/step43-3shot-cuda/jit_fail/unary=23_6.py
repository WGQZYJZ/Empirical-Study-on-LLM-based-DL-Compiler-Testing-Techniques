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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(2, 2, 5, stride=2, padding=0)
        self.conv = torch.nn.Conv2d(1, 1, 3, stride=1)

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = self.conv(v1)
        v3 = torch.tanh(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 2, 6, 6)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 2, 15, 15] to have 1 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 2, 15, 15)),), **{}):
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 2, 15, 15] to have 1 channels, but got 2 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''