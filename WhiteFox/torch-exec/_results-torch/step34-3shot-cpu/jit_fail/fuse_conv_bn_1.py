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
        self.conv1 = torch.nn.Conv2d(3, 3, 4)
        self.batchnorm2d = torch.nn.BatchNorm2d(3)
        self.tanh = torch.nn.Tanh()

    def forward(self, x0, x1):
        s = self.conv1(x0)
        t = self.batchnorm2d(s)
        u = self.tanh(t) + x1
        return t



func = Model().to('cpu')


x0 = torch.rand((1, 3, 6, 6))

x1 = torch.rand((1, 3, 6, 6))

test_inputs = [x0, x1]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (6) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 3, 3, 3)), FakeTensor(..., size=(1, 3, 6, 6))), **{}):
Attempting to broadcast a dimension of length 6 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 6, 6]); but expected shape should be broadcastable to [1, 3, 3, 3]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''