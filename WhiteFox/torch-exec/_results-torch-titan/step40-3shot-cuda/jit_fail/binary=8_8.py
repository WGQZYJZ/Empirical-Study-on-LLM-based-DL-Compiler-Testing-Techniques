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
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(8)

    def forward(self, x1, x2, weight):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = torch.addmm(v1, v2, weight, beta=0.0, alpha=1.0)
        v4 = self.bn(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)



weight = torch.randn(8, 8)


test_inputs = [x1, x2, weight]

# JIT_FAIL
'''
direct:
mat1 must be a matrix, got 4-D tensor

jit:
Failed running call_function <built-in method addmm of type object at 0x7832502699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)), FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)), FakeTensor(..., device='cuda:0', size=(8, 8))), **{'beta': 0.0, 'alpha': 1.0}):
a must be 2D

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''