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
        y = x.view(x.shape[0], -1)
        z = x.view(x.shape[0], -1)
        w = torch.relu(z)
        return torch.cat((x, y), dim=1).tanh()



func = Model().to('cpu')


x = torch.randn(2, 32, 32, 32)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 4 and 2

jit:
Failed running call_function <built-in method cat of type object at 0x74d92e196ec0>(*((FakeTensor(..., size=(s0, s1, s2, s3)), FakeTensor(..., size=(s0, s1*s2*s3))),), **{'dim': 1}):
Number of dimensions of tensors must match.  Expected 4-D tensors, but got 2-D for tensor number 1 in the list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''