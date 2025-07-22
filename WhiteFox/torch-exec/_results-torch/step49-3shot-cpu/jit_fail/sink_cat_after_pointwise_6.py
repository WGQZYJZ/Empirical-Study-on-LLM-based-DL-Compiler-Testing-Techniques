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
        y = x + 1
        x = torch.cat((x, y), dim=1).view(x.shape[0], -1)
        y = x.view(-1)
        x = y.sigmoid() * torch.cat((x, y), dim=1)
        return x



func = Model().to('cpu')


x = torch.randn(2, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 2 and 1

jit:
Failed running call_function <built-in method cat of type object at 0x7bb726796ec0>(*((FakeTensor(..., size=(s0, 2*s1*s2)), FakeTensor(..., size=(2*s0*s1*s2,))),), **{'dim': 1}):
Number of dimensions of tensors must match.  Expected 2-D tensors, but got 1-D for tensor number 1 in the list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''