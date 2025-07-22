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

    def forward(self, x):
        y1 = torch.cat((x, x), dim=1).view(2, 6)
        y2 = torch.cat((y1, x), dim=1)
        y3 = torch.relu(y2)
        y4 = torch.cat((y3, x), dim=1).tanh()
        return y4



func = Model().to('cpu')


x = torch.randn(1, 3, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 2 and 3

jit:
Failed running call_function <built-in method cat of type object at 0x7fc3f6d96ec0>(*((FakeTensor(..., size=(2, s0*s1)), FakeTensor(..., size=(1, s0, s1))),), **{'dim': 1}):
Number of dimensions of tensors must match.  Expected 2-D tensors, but got 3-D for tensor number 1 in the list

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''