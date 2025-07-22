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
        v2 = torch.mm(x2, x1)
        return torch.cat([v1, v1, v2, v1], 1)



func = Model().to('cpu')


x1 = torch.randn(1, 3)

x2 = torch.randn(3, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 1 but got size 3 for tensor number 2 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7ee98b596ec0>(*([FakeTensor(..., size=(1, 1)), FakeTensor(..., size=(1, 1)), FakeTensor(..., size=(s0, s0)), FakeTensor(..., size=(1, 1))], 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 1 in dimension 0 but got s0 for tensor number 2 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''