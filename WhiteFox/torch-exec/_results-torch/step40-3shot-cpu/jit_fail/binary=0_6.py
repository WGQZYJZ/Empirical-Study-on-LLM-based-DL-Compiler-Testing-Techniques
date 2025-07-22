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
        self.conv = torch.nn.Conv2d(3, 7, 1, stride=1, padding=1)
        self.t1 = torch.nn.Sigmoid()
        self.conv2 = torch.nn.Conv2d(7, 2, 1, stride=1, padding=1)

    def forward(self, x1, other=2, padding1=None):
        t1 = self.t1(self.conv(x1))
        if padding1 == None:
            padding1 = torch.randn(1, 5, 5, 5)
        v2 = other * t1
        v1 = v2 + padding1
        return self.conv2(v1)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 10, 10)

x2 = torch.randn(1, 1, 1, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (12) must match the size of tensor b (5) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 7, 12, 12)), FakeTensor(..., size=(1, 5, 5, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([1, 5, 5, 5]); but expected shape should be broadcastable to [1, 7, 12, 12]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''