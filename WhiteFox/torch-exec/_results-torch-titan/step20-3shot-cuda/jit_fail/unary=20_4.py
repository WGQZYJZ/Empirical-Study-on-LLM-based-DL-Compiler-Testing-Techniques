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
        self.conv = torch.nn.Conv2d(32, 192, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0), dilation=(1, 1), groups=1, bias=True, padding_mode='zeros')
        self.conv_transpose = torch.nn.ConvTranspose2d(96, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), dilation=(1, 1), groups=1, bias=True, padding_mode='zeros')

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.conv_transpose(v4)
        v6 = torch.sigmoid(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 96, 96, 192)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [192, 32, 1, 1], expected input[1, 96, 96, 192] to have 32 channels, but got 96 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 96, 96, 192)),), **{}):
Given groups=1, weight of size [192, 32, 1, 1], expected input[1, 96, 96, 192] to have 32 channels, but got 96 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''