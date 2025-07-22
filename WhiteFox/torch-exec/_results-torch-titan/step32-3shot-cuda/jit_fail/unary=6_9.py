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
        self.conv = torch.nn.Conv3d(3, 3, 3, stride=0, padding=0, dilation=1)
        self.maxpool = torch.nn.MaxPool3d(2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (3 + v1)
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = (v1 * v4)
        v6 = (v5 / 6)
        v7 = self.maxpool(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(2, 3, 7, 7, 7)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
non-positive stride is not supported

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(2, 3, 7, 7, 7)),), **{}):
non-positive stride is not supported

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''