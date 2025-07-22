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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.avg1 = torch.nn.AvgPool2d(kernel_size=1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.avg2 = torch.nn.AvgPool2d(kernel_size=1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.avg1(v1)
        v3 = self.conv2(x2)
        v4 = self.avg2(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
pad should be at most half of kernel size, but got pad=1 and kernel_size=1

jit:
Failed running call_module L__self___avg1(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)),), **{}):
pad should be at most half of kernel size, but got pad=1 and kernel_size=1

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''