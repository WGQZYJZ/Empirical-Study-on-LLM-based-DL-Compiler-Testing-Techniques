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

    def forward(self, x1, x2):
        v1 = torch.mm(x2, x1)
        v2 = v1.unsqueeze(-1)
        v3 = v2.squeeze(1)
        return v3



func = Model().to('cpu')


x1 = torch.randn(2, 3)

x2 = torch.randn(3, 4)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x4 and 2x3)

jit:
Failed running call_function <built-in method mm of type object at 0x7f3cf0996ec0>(*(FakeTensor(..., size=(3, 4)), FakeTensor(..., size=(2, 3))), **{}):
a and b must have same reduction dim, but got [3, 4] X [2, 3].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''