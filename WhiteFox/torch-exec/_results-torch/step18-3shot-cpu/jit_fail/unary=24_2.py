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
        self.conv1 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1 > 0
        v3 = v1 * 0.001
        v4 = torch.where(v2, v1, v3)
        v5 = self.conv2(x)
        v6 = v5 > 0
        x = v6 * 0.1
        v7 = torch.where(v4, v4, v3)
        v8 = self.conv3(v7)
        v9 = v8 > 0
        v10 = v8 * 0.1
        v11 = torch.where(v9, v8, v10)
        return v11



func = Model().to('cpu')


x1 = torch.randn(2, 8, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
where expected condition to be a boolean tensor, but got a tensor with dtype Float

jit:
Failed running call_function <built-in method where of type object at 0x73b187d96ec0>(*(FakeTensor(..., size=(2, 8, 66, 66)), FakeTensor(..., size=(2, 8, 66, 66)), FakeTensor(..., size=(2, 8, 66, 66))), **{}):
expected predicate to be bool, got torch.float32

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''