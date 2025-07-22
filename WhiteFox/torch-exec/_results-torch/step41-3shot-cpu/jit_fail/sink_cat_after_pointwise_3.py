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

    def forward(self, x, x1):
        x = x.view(x.shape[0], -1)
        x = torch.cat((x, x1), dim=1)
        x = x.view(x.shape[0], 2, -1)
        y = torch.tanh(x)
        return y if y.shape != (1,) else y



func = Model().to('cpu')


x = torch.randn(2, 1, 8)

x1 = torch.randn(2, 1, 8)

test_inputs = [x, x1]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 2 and 3

jit:
Failed running call_function <built-in method cat of type object at 0x769584596ec0>(*((FakeTensor(..., size=(s0, s1)), FakeTensor(..., size=(s2, 1, s3))),), **{'dim': 1}):
Number of dimensions of tensors must match.  Expected 2-D tensors, but got 3-D for tensor number 1 in the list

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''