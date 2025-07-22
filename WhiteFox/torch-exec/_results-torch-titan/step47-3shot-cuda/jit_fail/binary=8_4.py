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
        self.conv1 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 32, 1, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(16)

    def forward(self, x):
        v = []
        v.append(self.conv1(x))
        v.append(self.conv2(x))
        v.append(self.conv1(x))
        v.append(self.conv2(x))
        v1 = torch.cat(v, dim=1)
        return self.bn(v1)




func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 96 elements not 16

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(1, 96, 66, 66)),), **{}):
running_mean should contain 96 elements not 16

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''