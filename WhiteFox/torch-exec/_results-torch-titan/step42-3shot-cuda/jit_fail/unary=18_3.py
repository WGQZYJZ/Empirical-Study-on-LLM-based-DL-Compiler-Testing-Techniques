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
        self.bn = torch.nn.BatchNorm2d(2)
        self.conv1 = torch.nn.Conv2d(2, 4, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(2, 4, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(self.bn(x1))
        v2 = torch.sigmoid(v1)
        v3 = self.bn(self.conv2(x1))
        v4 = torch.sigmoid(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 2, 128, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 4 elements not 2

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(1, 4, 128, 128)),), **{}):
running_mean should contain 4 elements not 2

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''