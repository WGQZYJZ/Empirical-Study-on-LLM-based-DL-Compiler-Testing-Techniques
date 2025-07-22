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
        t1 = torch.mm(x1, x2)
        t2 = torch.cat([t1, t1, t1], 1)
        t3 = torch.cat([t2, t2], 1)
        t4 = torch.cat([t3, t3, t3, t3], 1)
        t5 = torch.cat([t1, t2, t3, t4], 0)
        return torch.cat([t5, t5], 1)



func = Model().to('cpu')


x1 = torch.randn(4, 10)

x2 = torch.randn(10, 10)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 10 but got size 30 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7ca2ad996ec0>(*([FakeTensor(..., size=(4, s1)), FakeTensor(..., size=(4, 3*s1)), FakeTensor(..., size=(4, 6*s1)), FakeTensor(..., size=(4, 24*s1))], 0), **{}):
Sizes of tensors must match except in dimension 0. Expected s1 in dimension 1 but got 3*s1 for tensor number 1 in the list

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''