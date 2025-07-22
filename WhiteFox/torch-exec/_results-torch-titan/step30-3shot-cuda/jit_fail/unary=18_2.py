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
        self.conv1 = torch.nn.Conv2d(1, 64, (64, 32), stride=(62, 30), padding=(0, 0))
        self.conv2 = torch.nn.Conv2d(64, 256, (16, 21), stride=(16, 21), padding=(0, 0))

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.sigmoid(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 1, 512, 211)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (8 x 6). Kernel size: (16 x 21). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 64, 8, 6)),), **{}):
Calculated padded input size per channel: (8 x 6). Kernel size: (16 x 21). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''