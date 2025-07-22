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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2, self.conv.weight.data)
        v2 = torch.cat([v1], dim=1)
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 256, 14, 14)

x2 = torch.randn(256, 512, 1, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 must be a matrix, got 4-D tensor

jit:
Failed running call_function <built-in method addmm of type object at 0x71e598796ec0>(*(FakeTensor(..., size=(1, 256, 14, 14)), FakeTensor(..., size=(256, 512, 1, 1)), FakeTensor(..., size=(8, 3, 1, 1))), **{}):
a must be 2D

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''