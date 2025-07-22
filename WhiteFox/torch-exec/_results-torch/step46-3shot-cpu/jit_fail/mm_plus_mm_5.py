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

    def forward(self, input):
        t1 = torch.mm(input[:, :, :], input[:, :, :])
        t2 = torch.mm(input[:, :, :], input[:, :, :])
        t3 = torch.mm(input[:, :, :], input[:, :, :])
        t4 = torch.mm(input[:, :, :], input[:, :, :])
        t5 = torch.mm(input[:, :, :], input[:, :, :])
        return t1 + t2 + t3 + t4 + t5



func = Model().to('cpu')


input = torch.randn(20, 3, 4)

test_inputs = [input]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x7b1953796ec0>(*(FakeTensor(..., size=(s0, s1, s2)), FakeTensor(..., size=(s0, s1, s2))), **{}):
a must be 2D

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''