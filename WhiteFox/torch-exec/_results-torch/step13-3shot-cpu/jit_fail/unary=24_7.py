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

    def forward(self, x):
        v1 = torch.nn.functional.conv1d(x, weight=torch.zeros([8, 1, 10], dtype=torch.float), bias=torch.zeros(8, dtype=torch.float))
        v2 = v1 > 0
        v3 = v1 * 10
        v4 = torch.where(v2, v1, v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 8, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 1, 10], expected input[1, 8, 128] to have 1 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv1d of type object at 0x7ff350796ec0>(*(FakeTensor(..., size=(1, 8, 128)),), **{'weight': FakeTensor(..., size=(8, 1, 10)), 'bias': FakeTensor(..., size=(8,))}):
Invalid channel dimensions

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''