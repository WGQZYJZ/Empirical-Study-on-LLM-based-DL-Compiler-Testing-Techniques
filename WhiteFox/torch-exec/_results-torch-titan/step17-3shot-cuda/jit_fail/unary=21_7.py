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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_a = torch.nn.Conv2d(3, 40, 33, stride=5, padding=1, dilation=8)
        self.conv_b = torch.nn.ConvTranspose2d(40, 3, 14)

    def forward(self, x):
        v1 = self.conv_a(x)
        v2 = torch.tanh(v1)
        v3 = self.conv_b(v2)
        return v3




func = ModelTanh().to('cuda')



x = torch.randn(2, 3, 57, 50)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (59 x 52). Kernel size: (257 x 257). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv_a(*(FakeTensor(..., device='cuda:0', size=(2, 3, 57, 50)),), **{}):
Calculated padded input size per channel: (59 x 52). Kernel size: (257 x 257). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''