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
        v1 = torch.mm(x1, x2)
        v10 = v1.repeat(2, 1)
        v2 = torch.mm(x1, x2)
        v20 = v2.repeat(2, 1)
        t1 = torch.cat([v1, v2], 1)
        t2 = torch.cat([v10, v20], 1)
        t3 = torch.cat([t1, t2], 0)
        t4 = torch.cat([t1, t2], 1)
        return torch.cat([t3, t4], 1)



func = Model().to('cpu')


x1 = torch.randn(2, 2)

x2 = torch.randn(2, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 2 but got size 4 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x764b5ab96ec0>(*([FakeTensor(..., size=(s2, 2*s1)), FakeTensor(..., size=(2*s2, 2*s1))], 1), **{}):
Sizes of tensors must match except in dimension 1. Expected s2 in dimension 0 but got 2*s2 for tensor number 1 in the list

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''