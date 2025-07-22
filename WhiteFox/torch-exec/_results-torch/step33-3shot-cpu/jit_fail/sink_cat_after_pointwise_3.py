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

    def forward(self, x0):
        x1 = torch.transpose(x0, 0, -1).reshape(x0.shape[1], -1)
        x2 = torch.cat((x1, x0), dim=0)
        return x2



func = Model().to('cpu')


x = torch.randn(2, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 2 and 3

jit:
Failed running call_function <built-in method cat of type object at 0x71883c996ec0>(*((FakeTensor(..., size=(2, 4)), FakeTensor(..., size=(2, 2, 2))),), **{'dim': 0}):
Number of dimensions of tensors must match.  Expected 2-D tensors, but got 3-D for tensor number 1 in the list

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''