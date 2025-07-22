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
        self.conv1 = torch.nn.Conv2d(16, 8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 8, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 16, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = x1 + v1
        v4 = x2 + v2
        v4 = self.conv3(v4)
        v5 = self.conv4(v3)
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 16, 16, 16)

x2 = torch.randn(1, 16, 16, 16)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 16, 16, 16)), FakeTensor(..., size=(1, 8, 16, 16))), **{}):
Attempting to broadcast a dimension of length 8 at -3! Mismatching argument at index 1 had torch.Size([1, 8, 16, 16]); but expected shape should be broadcastable to [1, 16, 16, 16]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''