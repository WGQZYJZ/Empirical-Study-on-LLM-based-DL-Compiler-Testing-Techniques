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
        self.conv1 = torch.nn.Conv2d(16, 16, 15, stride=1, padding=0)

    def forward(self, x1, x3):
        v1 = self.conv1(x1)
        v2 = (v1 + x3)
        v3 = torch.relu(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 16, 1, 128)



x3 = torch.randn(1, 16, 128, 128)


test_inputs = [x1, x3]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 128). Kernel size: (15 x 15). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 16, 1, 128)),), **{}):
Calculated padded input size per channel: (1 x 128). Kernel size: (15 x 15). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''