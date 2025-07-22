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
        self.conv = torch.nn.Conv2d(3, 3, 3, stride=2, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(3)
        self.bn2 = torch.nn.BatchNorm1d(3)
        self.avgpool = torch.nn.AvgPool2d(3, stride=1, padding=1)

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = self.bn1(t1)
        t3 = F.relu((3 + t2))
        t4 = torch.clamp(t3, 0, 6)
        t5 = (t1 * t4)
        t6 = (t5 / 6)
        t7 = self.bn2(t6)
        t8 = torch.relu(t7)
        t9 = self.avgpool(t8)
        return t9




func = Model().to('cuda')



x1 = torch.randn(2, 3, 15, 15)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected 2D or 3D input (got 4D input)

jit:
Failed running call_module L__self___bn2(*(FakeTensor(..., device='cuda:0', size=(2, 3, 8, 8)),), **{}):
expected 2D or 3D input (got 4D input)

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''