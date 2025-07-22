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
        self.conv = torch.nn.Conv2d(3, 7, 16, stride=3, padding=5, dilation=3)
        self.tconv1 = torch.nn.ConvTranspose2d(7, 13, 4, stride=2)
        self.tconv2 = torch.nn.ConvTranspose2d(13, 19, 5, stride=3, padding=4)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.tanh(v1)
        v3 = self.tconv1(v2)
        v4 = torch.tanh(v3)
        return self.tconv2(v4)




func = ModelTanh().to('cuda')



x = torch.randn(1, 3, 4, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (14 x 74). Kernel size: (46 x 46). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 4, 64)),), **{}):
Calculated padded input size per channel: (14 x 74). Kernel size: (46 x 46). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''