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
        x1 = x.view(x.shape + (1,))
        x2 = torch.transpose(x1, 0, 2)
        x3 = torch.cat((x2, x2), dim=0)
        x4 = torch.cat((x1, x3), dim=1)
        x5 = x4.sum(dim=2)
        x6 = torch.cat((x5, x5), dim=0)
        return 2.0 * x6



func = Model().to('cpu')


x = torch.randn(2, 3, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 2 but got size 4 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7dc40ff96ec0>(*((FakeTensor(..., size=(s0, s1, s2, s3, 1)), FakeTensor(..., size=(2*s2, s1, s0, s3, 1))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected s0 in dimension 0 but got 2*s2 for tensor number 1 in the list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''