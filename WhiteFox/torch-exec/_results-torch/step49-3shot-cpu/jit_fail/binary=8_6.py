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
        self.conv1 = torch.nn.Conv2d(3, 16, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 16, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(16, 3, 1, stride=1, padding=1)

    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = self.conv3(x3)
        v5 = v1 + v2 + v3
        v6 = self.conv4(v5)
        v8 = v1 + v2
        v9 = v1 + v3
        v10 = v2 + v3
        v11 = v8 + v9 + v10
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 16, 16)

x2 = torch.randn(1, 3, 16, 16)

x3 = torch.randn(1, 3, 16, 16)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (18) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 16, 16, 16)), FakeTensor(..., size=(1, 16, 18, 18))), **{}):
Attempting to broadcast a dimension of length 18 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 18, 18]); but expected shape should be broadcastable to [1, 16, 16, 16]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''