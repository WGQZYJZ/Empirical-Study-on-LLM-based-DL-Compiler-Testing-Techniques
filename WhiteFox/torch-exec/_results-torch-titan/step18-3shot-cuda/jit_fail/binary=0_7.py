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
        self.conv = torch.nn.Conv2d(13, 13, 1, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(13)
        self.conv_ = torch.nn.Conv2d(13, 13, 1, stride=1)
        self.relu = torch.nn.ReLU()

    def forward(self, x1, padding1=None):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        v3 = torch.cat((v1, v2), axis=1)
        v4 = self.conv_(v3)
        v5 = self.relu(v2)
        v6 = (v5 + v4)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 13, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [13, 13, 1, 1], expected input[1, 26, 66, 66] to have 13 channels, but got 26 channels instead

jit:
Failed running call_module L__self___conv_(*(FakeTensor(..., device='cuda:0', size=(1, 26, 66, 66)),), **{}):
Given groups=1, weight of size [13, 13, 1, 1], expected input[1, 26, 66, 66] to have 13 channels, but got 26 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''