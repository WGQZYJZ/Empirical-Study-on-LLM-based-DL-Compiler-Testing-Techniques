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
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1, x2, x3):
        v1 = self.linear(x1)
        v2 = v1 + x2
        v3 = F.relu(v2)
        v4 = self.linear(v3)
        v5 = v4 + x2
        v6 = v4 * v5
        v7 = v3 - v6
        v8 = self.linear(v7)
        v9 = v8 * 0.3
        v10 = torch.abs(v9)
        v11 = F.sigmoid(v10)
        return v11


func = Model().to('cpu')


x1 = torch.randn(1, 3)

x2 = torch.randn(1, 3)

x3 = torch.randn(1, 3)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 4)), FakeTensor(..., size=(1, s1))), **{}):
The size of tensor a (4) must match the size of tensor b (s1) at non-singleton dimension 1)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''