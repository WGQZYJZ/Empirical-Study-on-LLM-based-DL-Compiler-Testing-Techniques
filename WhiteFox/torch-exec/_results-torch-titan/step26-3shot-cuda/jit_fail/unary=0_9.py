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
        self.conv1 = torch.nn.Conv2d(128, 4, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=0)

    def forward(self, x2, x3):
        v1 = self.conv1(x3)
        v2 = self.conv2(x2)
        v3 = torch.relu((v2 + v1))
        return v3




func = Model().to('cuda')



x2 = torch.randn(7, 128, 24, 24)



x3 = torch.randn(7, 16, 4, 4)


test_inputs = [x2, x3]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 128, 1, 1], expected input[7, 16, 4, 4] to have 128 channels, but got 16 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(7, 16, 4, 4)),), **{}):
Given groups=1, weight of size [4, 128, 1, 1], expected input[7, 16, 4, 4] to have 128 channels, but got 16 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''