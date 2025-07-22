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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv_t1 = torch.nn.ConvTranspose3d(1, 1, 2, stride=2)
        self.conv_t2 = torch.nn.ConvTranspose3d(1, 1, 2, stride=2)
        self.negative_slope = negative_slope

    def forward(self, x):
        t1 = self.conv_t1(x)
        t2 = torch.le(t1, 0.9)
        t3 = t1 * self.negative_slope
        t4 = torch.where(t2, t1, t3)
        t5 = self.conv_t2(t4)
        t6 = torch.le(t5, 0.708)
        t7 = t5 * self.negative_slope
        t8 = torch.where(t6, t4, t7)
        return t8


negative_slope = 0.13

func = Model(negative_slope).to('cpu')


x = torch.randn(4, 1, 2, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (4) at non-singleton dimension 4

jit:
Failed running call_function <built-in method where of type object at 0x708df0796ec0>(*(FakeTensor(..., size=(s0, 1, 4*s1, 4*s2, 4*s3), dtype=torch.bool), FakeTensor(..., size=(s0, 1, 2*s1, 2*s2, 2*s3)), FakeTensor(..., size=(s0, 1, 4*s1, 4*s2, 4*s3))), **{}):
Attempting to broadcast a dimension of length 2*s3 at -1! Mismatching argument at index 1 had torch.Size([s0, 1, 2*s1, 2*s2, 2*s3]); but expected shape should be broadcastable to [s0, 1, 4*s1, 4*s2, 4*s3]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''