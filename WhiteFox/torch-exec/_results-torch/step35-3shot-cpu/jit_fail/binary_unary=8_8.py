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
        self.conv1 = torch.nn.Conv2d(3, 7, 5, stride=1, padding=2)
        self.conv2 = torch.nn.Conv2d(7, 15, 5, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 + torch.randn(v1.size())
        v3 = torch.relu(v2)
        v4 = self.conv2(v3)
        v5 = v2 + torch.randn(v4.size())
        v6 = v4 + torch.randn(v4.size())
        v7 = torch.relu(v5)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (7) must match the size of tensor b (15) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 7, 64, 64)), FakeTensor(..., size=(1, 15, 64, 64))), **{}):
Attempting to broadcast a dimension of length 15 at -3! Mismatching argument at index 1 had torch.Size([1, 15, 64, 64]); but expected shape should be broadcastable to [1, 7, 64, 64]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''