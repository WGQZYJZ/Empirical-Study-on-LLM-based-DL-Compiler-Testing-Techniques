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
        self.conv = torch.nn.Conv2d(20, 20, kernel_size=(5, 5), stride=(2, 2), bias=False)
        self.batch_norm_0 = torch.nn.BatchNorm2d(20, affine=True)
        self.conv_1 = torch.nn.Conv2d(20, 40, kernel_size=(5, 5), stride=(1, 1), bias=False)
        self.batch_norm_1 = torch.nn.BatchNorm2d(40, affine=True)

    def forward(self, x):
        x = self.conv(x)
        x = self.batch_norm_0(x)
        x = self.conv_1(x)
        x = self.batch_norm_1(x)
        return x




func = Model().to('cuda')



x = torch.randn(1, 20, 6, 6)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 1). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv_1(*(FakeTensor(..., device='cuda:0', size=(1, 20, 1, 1)),), **{}):
Calculated padded input size per channel: (1 x 1). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''