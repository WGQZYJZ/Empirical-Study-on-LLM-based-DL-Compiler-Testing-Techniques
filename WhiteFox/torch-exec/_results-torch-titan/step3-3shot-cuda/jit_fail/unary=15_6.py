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
        self.conv = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(8)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        v3 = torch.relu(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 128, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 16 elements not 8

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(1, 16, 130, 130)),), **{}):
running_mean should contain 16 elements not 8

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''