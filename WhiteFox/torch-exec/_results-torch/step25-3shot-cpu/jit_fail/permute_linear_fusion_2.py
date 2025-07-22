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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v9 = torch.randn(1, 2, 1)
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        x2 = torch.nn.functional.gelu(v2)
        x3 = x2.size()
        v4 = torch.cat([v9, x2])
        v5 = v4.view(-1)
        v3 = torch.cat([v5, x2])
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 1 but got size 2 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x799354d96ec0>(*([FakeTensor(..., size=(1, 2, 1)), FakeTensor(..., size=(1, 2, 2))],), **{}):
Sizes of tensors must match except in dimension 0. Expected 1 in dimension 2 but got 2 for tensor number 1 in the list

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''