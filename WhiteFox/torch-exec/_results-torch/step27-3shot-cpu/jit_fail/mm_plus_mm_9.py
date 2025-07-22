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

    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2) + torch.mm(x3, x4)
        v2 = torch.mm(x3, x4) + torch.mm(x1, x2)
        v3 = v1 * v2
        v4 = torch.mm(x2, x1) * torch.mm(x4, x3)
        return v3 + v4



func = Model().to('cpu')


x1 = torch.randn(65, 65)

x2 = torch.randn(65, 65)

x3 = torch.randn(3, 3)

x4 = torch.randn(3, 3)

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
The size of tensor a (65) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s2, s1)), FakeTensor(..., size=(s6, s5))), **{}):
The size of tensor a (s1) must match the size of tensor b (s5) at non-singleton dimension 1)

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''