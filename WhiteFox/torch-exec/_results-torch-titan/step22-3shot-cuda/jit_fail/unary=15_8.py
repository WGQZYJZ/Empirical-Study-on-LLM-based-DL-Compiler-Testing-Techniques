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
        self.conv_bn = torch.nn.Conv2d(3, 32, 3, stride=1, padding=1)
        self.conv_relu = torch.nn.Conv2d(3, 64, 7, stride=1, padding_mode='zeros')

    def forward(self, x1):
        v1 = self.conv_bn(x1)
        v2 = torch.relu(v1)
        v3 = self.conv_relu(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 3, 7, 7], expected input[1, 32, 256, 256] to have 3 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv_relu(*(FakeTensor(..., device='cuda:0', size=(1, 32, 256, 256)),), **{}):
Given groups=1, weight of size [64, 3, 7, 7], expected input[1, 32, 256, 256] to have 3 channels, but got 32 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''