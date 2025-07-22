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
        v1 = torch.cat([torch.cat([torch.mm(x1, x2), torch.mm(x1, x2)], 0), torch.cat([torch.mm(x1, x2), torch.mm(x1, x2)], 0), torch.cat([torch.mm(x1, x2), torch.mm(x1, x2)], 0)], 1)
        v2 = torch.cat([torch.mm(x1, x2), v1, torch.mm(x1, x2)], 0)
        v3 = torch.cat([torch.mm(x1, x2), torch.mm(x1, x2), v2], 1)
        v4 = torch.cat([v3, v3], 0)
        return v4



func = Model().to('cpu')


x1 = torch.randn(2, 4)

x2 = torch.randn(4, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 1 but got size 3 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7fc972b96ec0>(*([FakeTensor(..., size=(s1, 1)), FakeTensor(..., size=(2*s1, 3)), FakeTensor(..., size=(s1, 1))], 0), **{}):
Sizes of tensors must match except in dimension 0. Expected 1 in dimension 1 but got 3 for tensor number 1 in the list

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''