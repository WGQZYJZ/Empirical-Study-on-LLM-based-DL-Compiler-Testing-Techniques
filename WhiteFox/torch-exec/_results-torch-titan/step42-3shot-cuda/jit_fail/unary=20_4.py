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
        self.conv_t = torch.nn.ConvTranspose3d(32, 1024, kernel_size=3, stride=2, padding=1)
        self.conv_t = torch.nn.ConvTranspose3d(1024, 512, kernel_size=3, stride=1, padding=1)
        self.conv_t = torch.nn.ConvTranspose3d(512, 512, kernel_size=3, stride=2, padding=1)
        self.conv_t = torch.nn.ConvTranspose3d(512, 256, kernel_size=3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = torch.sigmoid(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 32, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [512, 256, 3, 3, 3], expected input[1, 1, 32, 64, 64] to have 512 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(1, 32, 64, 64)),), **{}):
Given transposed=1, weight of size [512, 256, 3, 3, 3], expected input[1, 1, 32, 64, 64] to have 512 channels, but got 1 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''