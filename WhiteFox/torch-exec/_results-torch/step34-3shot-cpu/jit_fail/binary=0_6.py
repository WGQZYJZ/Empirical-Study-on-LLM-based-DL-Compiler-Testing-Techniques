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
        self.conv1 = torch.nn.Conv2d(1, 3, 3, stride=1, padding=2)
        self.conv2 = torch.nn.Conv2d(3, 12, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(8, 14, 1, stride=1, padding=0)

    def forward(self, x1, other=None):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v1)
        v4 = self.conv4(v3)
        v5 = v2 + v4
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 1, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (12) must match the size of tensor b (14) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 12, 66, 66)), FakeTensor(..., size=(1, 14, 66, 66))), **{}):
Attempting to broadcast a dimension of length 14 at -3! Mismatching argument at index 1 had torch.Size([1, 14, 66, 66]); but expected shape should be broadcastable to [1, 12, 66, 66]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''