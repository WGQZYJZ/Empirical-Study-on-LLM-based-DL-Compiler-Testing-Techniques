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
        self.conv_transpose = torch.nn.ConvTranspose2d(4, 4, 1, stride=1)
        self.conv = torch.nn.Conv2d(4, 5, (3, 5), stride=2)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tanh(v1)
        v3 = self.conv(v2)
        v4 = torch.tanh(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 4, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (4 x 4). Kernel size: (3 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 4, 4, 4)),), **{}):
Calculated padded input size per channel: (4 x 4). Kernel size: (3 x 5). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''