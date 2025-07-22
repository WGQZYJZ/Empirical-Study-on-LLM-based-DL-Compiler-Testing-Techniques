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
        self.conv1 = torch.nn.Conv2d(2, 3, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.sigmoid(v2)
        v4 = v1 * v3
        return v4



func = Model().to('cpu')


x = torch.randn(1, 2, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (66) must match the size of tensor b (68) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 3, s1 + 2, s2 + 2)), FakeTensor(..., size=(1, 3, s1 + 4, s2 + 4))), **{}):
The size of tensor a (s2 + 2) must match the size of tensor b (s2 + 4) at non-singleton dimension 3)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''