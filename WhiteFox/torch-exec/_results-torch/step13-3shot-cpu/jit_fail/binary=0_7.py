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
        self.conv1 = torch.nn.Conv2d(10, 20, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(20, 5, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(15, 10, 1, stride=1, padding=1)

    def forward(self, x1, some_parameter=None):
        v1 = self.conv1(x1[:5].clone())
        v2 = self.conv2(x1 + v1)
        v3 = self.conv3(v1 + v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(2, 10, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (66) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(2, 10, 64, 64)), FakeTensor(..., size=(2, 20, 66, 66))), **{}):
Attempting to broadcast a dimension of length 66 at -1! Mismatching argument at index 1 had torch.Size([2, 20, 66, 66]); but expected shape should be broadcastable to [2, 10, 64, 64]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''