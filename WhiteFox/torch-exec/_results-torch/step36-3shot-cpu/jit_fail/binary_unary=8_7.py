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
        self.conv1 = torch.nn.Conv2d(1, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v1)
        v4 = self.conv3(v2)
        v5 = v1 + v2 + v3 + v4
        v6 = torch.relu(v5)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 1, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (66) must match the size of tensor b (68) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, s0 + 2, s1 + 2)), FakeTensor(..., size=(1, 8, s0 + 4, s1 + 4))), **{}):
The size of tensor a (s1 + 2) must match the size of tensor b (s1 + 4) at non-singleton dimension 3)

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''