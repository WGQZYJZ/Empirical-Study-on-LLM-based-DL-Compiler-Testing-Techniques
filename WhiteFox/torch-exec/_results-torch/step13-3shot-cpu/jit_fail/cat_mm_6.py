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
        v2 = torch.mm(x1, x2)
        return torch.cat([v1.flatten(), v1])



func = Model().to('cpu')


x1 = torch.randn(3, 2)

x2 = torch.randn(2, 5)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 1 and 2

jit:
Failed running call_function <built-in method cat of type object at 0x7ab3fb596ec0>(*([FakeTensor(..., size=(s1*s2,)), FakeTensor(..., size=(s2, s1))],), **{}):
Number of dimensions of tensors must match.  Expected 2-D tensors, but got 1-D for tensor number 0 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''