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
        self.conv1 = torch.nn.Conv2d(128, 16, kernel_size=128, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(16, 16, kernel_size=128, stride=1, padding=0)
        self.convT = torch.nn.ConvTranspose2d(16, 16, kernel_size=19, stride=1, padding=0)

    def forward(self, x1):
        r1 = self.conv1(x1)
        r2 = self.conv2(r1)
        r3 = self.convT(r2)
        return r3




func = Model().to('cuda')



x1 = torch.randn(1, 128, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (28 x 28). Kernel size: (128 x 128). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 128, 28, 28)),), **{}):
Calculated padded input size per channel: (28 x 28). Kernel size: (128 x 128). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''