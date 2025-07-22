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
        self.conv1 = torch.nn.Conv2d(4, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(4, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv1(x1) + self.conv1(x2)
        v2 = v1 - 2.0
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 4, 65, 65)

x2 = torch.randn(1, 4, 64, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (67) must match the size of tensor b (66) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, s1 + 2, s2 + 2)), FakeTensor(..., size=(1, 8, 66, 66))), **{}):
The size of tensor a (s2 + 2) must match the size of tensor b (66) at non-singleton dimension 3)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''