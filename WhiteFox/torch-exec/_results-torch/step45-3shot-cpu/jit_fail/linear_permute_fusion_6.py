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

    def forward(self, x1, x2, x3):
        v4 = torch.cat([x1, x2, x3], -1)
        v1 = v4.reshape(-1, 3, 3)
        v5 = v1.permute(0, 2, 1)
        v6 = torch.ones_like(v5)
        v7 = torch.matmul(v5.permute(0, 2, 1), v6.permute(0, 2, 1))
        v8 = v7.permute(0, 2, 1)
        v2 = torch.ones_like(v4)
        v9 = v2.reshape(-1, 3, 3)
        v10 = v9.permute(0, 2, 1)
        v3 = torch.ones_like(v4)
        v11 = v3.reshape(-1, 3, 3)
        v12 = v11.permute(0, 2, 1)
        v13 = torch.mm(v12, v10)
        return v8 + v13



func = Model().to('cpu')


x1 = torch.randn(1, 2, 3)

x2 = torch.randn(1, 4, 3)

x3 = torch.randn(1, 6, 3)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 2. Expected size 2 but got size 4 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x703b47f96ec0>(*([FakeTensor(..., size=(1, 2, 3)), FakeTensor(..., size=(1, 4, 3)), FakeTensor(..., size=(1, 6, 3))], -1), **{}):
Sizes of tensors must match except in dimension 2. Expected 2 in dimension 1 but got 4 for tensor number 1 in the list

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''