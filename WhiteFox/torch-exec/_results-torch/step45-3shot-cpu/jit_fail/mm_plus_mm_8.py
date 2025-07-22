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

    def forward(self, i1, i2, i3, i4):
        t1 = torch.bmm(i1, i2)
        t2 = torch.einsum('nc, mnc -> nm', i3, i4)
        t3 = t2 / t2.sum()
        return t1 + t3



func = Model().to('cpu')


i1 = torch.randn(6, 3, 5)

i2 = torch.randn(6, 5, 7)

i3 = torch.randn(3, 7)

i4 = torch.randn(6, 7, 5)

test_inputs = [i1, i2, i3, i4]

# JIT_FAIL
'''
direct:
einsum(): subscript n has size 7 for operand 1 which does not broadcast with previously seen size 3

jit:
Failed running call_function <function einsum at 0x76cc53f40040>(*('nc, mnc -> nm', FakeTensor(..., size=(3, 7)), FakeTensor(..., size=(6, 7, 5))), **{}):
einsum(): subscript n has size 7 for operand 1 which does not broadcast with previously seen size 3

from user code:
   File "<string>", line 17, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''