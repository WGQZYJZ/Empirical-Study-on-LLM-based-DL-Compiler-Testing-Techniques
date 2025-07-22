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
        self.conv1 = torch.nn.Conv2d(1, 64, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(64, 128, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(128, 128, 1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(128, 256, 1, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(256, 512, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v2)
        v5 = self.conv5(v4)
        v6 = torch.max(v2, 1)
        v7 = v5 + v6
        v8 = v7
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 1, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for +: 'Tensor' and 'torch.return_types.max'

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 512, 72, 72)), (FakeTensor(..., size=(1, 68, 68)), FakeTensor(..., size=(1, 68, 68), dtype=torch.int64))), **{}):
unsupported operand type(s) for +: 'FakeTensor' and 'tuple'

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''