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
        self.conv1 = torch.nn.Conv2d(3, 32, 3, stride=1, padding=1, dilation=1)
        self.conv2 = torch.nn.Conv2d(32, 16, 1, stride=2, padding=1, dilation=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = F.relu(v1)
        v3 = self.conv2(v2)
        v4 = F.relu(x1)
        v5 = torch.mul(v3, v4)
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (33) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in method mul of type object at 0x79a0df596ec0>(*(FakeTensor(..., size=(1, 16, (((s0 + 1)//2)) + 1, (((s1 + 1)//2)) + 1)), FakeTensor(..., size=(1, 3, s0, s1))), **{}):
The size of tensor a ((((s1 + 1)//2)) + 1) must match the size of tensor b (s1) at non-singleton dimension 3)

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''