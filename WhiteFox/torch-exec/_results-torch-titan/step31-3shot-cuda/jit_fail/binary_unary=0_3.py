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
        self.conv1 = torch.nn.Conv2d(24, 48, (1, 5), stride=(4, 1), padding=(1, 2))
        self.conv2 = torch.nn.Conv2d(48, 96, (1, 10), stride=(1, 5), padding=(0, 7))
        self.conv3 = torch.nn.Conv2d(96, 192, (1, 20), stride=(1, 10), padding=(0, 6))

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        return v3




func = Model().to('cuda')



x = torch.randn(1, 24, 47, 26)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (13 x 19). Kernel size: (1 x 20). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1, 96, 13, 7)),), **{}):
Calculated padded input size per channel: (13 x 19). Kernel size: (1 x 20). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''