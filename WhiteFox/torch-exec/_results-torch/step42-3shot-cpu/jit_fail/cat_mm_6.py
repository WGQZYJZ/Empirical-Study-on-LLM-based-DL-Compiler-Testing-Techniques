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

    def forward(self, x1, x2):
        a = None
        for i in range(100):
            with torch.no_grad():
                t = x1 + x2
        return torch.cat([a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a], 1)



func = Model().to('cpu')


x1 = torch.randn(5, 4)

x2 = torch.randn(5, 6)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (6) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0, s1)), FakeTensor(..., size=(s2, s3))), **{}):
The size of tensor a (s1) must match the size of tensor b (s3) at non-singleton dimension 1)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''