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
        self.conv_transpose_0 = torch.nn.ConvTranspose2d(381, 785, 2, stride=1, padding=0, dilation=1, groups=1)
        self.weight_0 = torch.nn.Parameter(torch.ones(785, 1, 2, 2))

    def forward(self, x1):
        v1 = self.conv_transpose_0(x1)
        v2 = self.weight_0
        v3 = v1 * v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 381, 100, 100)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (101) must match the size of tensor b (2) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 785, 101, 101)), Parameter(FakeTensor(..., size=(785, 1, 2, 2), requires_grad=True))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([785, 1, 2, 2]); but expected shape should be broadcastable to [1, 785, 101, 101]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''