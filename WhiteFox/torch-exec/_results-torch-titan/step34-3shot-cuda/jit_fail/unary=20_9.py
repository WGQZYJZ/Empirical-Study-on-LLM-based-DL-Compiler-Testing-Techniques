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
        self.conv_t = torch.nn.ConvTranspose2d(16, 16, kernel_size=(1, 1), stride=(1, 1))

    def forward(self, x1):
        v0 = x1.transpose(2, 1)
        v1 = self.conv_t(v0)
        v2 = v1.transpose(2, 1)
        v3 = torch.sigmoid(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 16, 24, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [16, 16, 1, 1], expected input[1, 24, 16, 32] to have 16 channels, but got 24 channels instead

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(1, 24, 16, 32)),), **{}):
Given transposed=1, weight of size [16, 16, 1, 1], expected input[1, 24, 16, 32] to have 16 channels, but got 24 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''