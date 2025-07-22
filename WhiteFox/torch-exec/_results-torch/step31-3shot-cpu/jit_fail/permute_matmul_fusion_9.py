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
        t2 = x2.permute(0, 3, 1, 2)
        t3 = x1.permute(0, 3, 1, 2)
        t5 = torch.bmm(t3, t2)
        v8 = t2.permute(0, 1, 3, 2)
        v9 = torch.bmm(t2, v8)
        t4 = x1.permute(0, 3, 1, 2)
        v6 = torch.bmm(t4, v8)
        return v9



func = Model().to('cpu')


x1 = torch.randn(1, 3, 2, 2)

x2 = torch.randn(1, 3, 2, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
batch1 must be a 3D tensor

jit:
Failed running call_function <built-in method bmm of type object at 0x7b0ea2396ec0>(*(FakeTensor(..., size=(1, s5, s3, s4)), FakeTensor(..., size=(1, s2, s0, s1))), **{}):
batch1 must be a 3D tensor

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''