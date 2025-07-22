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
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=2, padding=2, dilation=1)
        self.conv2 = torch.nn.Conv2d(3, 16, 2, stride=2, padding=1, dilation=3)
        self.conv3 = torch.nn.Conv2d(16, 32, 1, stride=2, padding=2, bias=False)
        self.conv4 = torch.nn.Conv2d(32, 64, 2, stride=1, padding=2, dilation=4, groups=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = torch.tanh(v1 + v2)
        v4 = self.conv3(v3)
        v5 = F.relu(v4)
        v6 = self.conv4(v5)
        v7 = F.relu(v6)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 3, 128, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (33) must match the size of tensor b (32) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, 65, 33)), FakeTensor(..., size=(1, 16, 64, 32))), **{}):
Attempting to broadcast a dimension of length 32 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 64, 32]); but expected shape should be broadcastable to [1, 8, 65, 33]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''