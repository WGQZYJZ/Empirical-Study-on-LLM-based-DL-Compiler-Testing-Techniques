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
        self.conv1 = torch.nn.Conv2d(2, 5, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(5, 5, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v11 = self.conv1(x2)
        v12 = v11 * 0.5
        v13 = v11 * 0.7071067811865476
        v14 = torch.erf(v13)
        v15 = v14 + 1
        v16 = v12 * v15
        v17 = torch.sum(v6 + v16)
        return v17



func = Model().to('cpu')


x1 = torch.randn(1, 2, 1, 15)

x2 = torch.randn(1, 2, 15, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (17) must match the size of tensor b (3) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 5, 3, s1 + 2)), FakeTensor(..., size=(1, 5, 17, 3))), **{}):
The size of tensor a (s1 + 2) must match the size of tensor b (3) at non-singleton dimension 3)

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''