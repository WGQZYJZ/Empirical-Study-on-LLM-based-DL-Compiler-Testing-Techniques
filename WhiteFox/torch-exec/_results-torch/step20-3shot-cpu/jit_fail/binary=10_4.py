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
        self.linear = torch.nn.Flatten()

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + x1
        return v2


func = Model().to('cpu')


x1 = torch.randn(8, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (12288) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0, s1*s2*s3)), FakeTensor(..., size=(s0, s1, s2, s3))), **{}):
The size of tensor a (s1*s2*s3) must match the size of tensor b (s3) at non-singleton dimension 3)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''