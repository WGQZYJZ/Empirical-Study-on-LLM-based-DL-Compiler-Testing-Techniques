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

    def forward(self, x, w0, w1, w2):
        y = torch.cat((x, w0.view(w0.size(0), -1)), dim=1)
        y = y + w1.view(w1.size(0), -1)
        return y.tanh() + w2.view(w2.size(0), -1).tanh()



func = Model().to('cpu')


w0 = torch.randn(64, 4096, 7, 7)

w1 = torch.randn(64, 4096, 1, 1)

w2 = torch.randn(64)

x = torch.randn(64, 3, 224, 224)

test_inputs = [w0, w1, w2, x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 4 and 2

jit:
Failed running call_function <built-in method cat of type object at 0x72803d596ec0>(*((FakeTensor(..., size=(s0, s1, s2, s3)), FakeTensor(..., size=(64, 4096))),), **{'dim': 1}):
Number of dimensions of tensors must match.  Expected 4-D tensors, but got 2-D for tensor number 1 in the list

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''