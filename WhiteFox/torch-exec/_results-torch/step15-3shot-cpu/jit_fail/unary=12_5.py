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
        self.conv1 = torch.nn.Conv2d(3, 16, 5, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 64, 3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(64, 64, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = torch.sigmoid(self.conv1(x1))
        v2 = torch.mul(self.conv2(v1), v1)
        v3 = torch.mul(self.conv3(v2), v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (15) must match the size of tensor b (30) at non-singleton dimension 3

jit:
Failed running call_function <built-in method mul of type object at 0x7dd621996ec0>(*(FakeTensor(..., size=(1, 64, 15, 15)), FakeTensor(..., size=(1, 16, 30, 30))), **{}):
Attempting to broadcast a dimension of length 30 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 30, 30]); but expected shape should be broadcastable to [1, 64, 15, 15]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''