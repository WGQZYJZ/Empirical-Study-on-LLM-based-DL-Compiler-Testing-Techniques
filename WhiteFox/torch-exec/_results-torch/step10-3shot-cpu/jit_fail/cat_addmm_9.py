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
        self.conv0 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=0)
        self.conv1 = torch.nn.Conv2d(3, 6, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(6, 6, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv0(x1)
        v2 = self.conv1(v1)
        v3 = self.conv2(v2)
        v4 = torch.addmm(v3, v2, v1 * 8)
        v5 = torch.cat([v2, v4], dim=1)
        return v5


func = Model().to('cpu')


x1 = torch.randn(1, 3, 128, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 must be a matrix, got 4-D tensor

jit:
Failed running call_function <built-in method addmm of type object at 0x71ddb4396ec0>(*(FakeTensor(..., size=(1, 6, 128, 128)), FakeTensor(..., size=(1, 6, 128, 128)), FakeTensor(..., size=(1, 3, 128, 128))), **{}):
a must be 2D

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''