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
        if y.dim() - 2 > 2:
            y = y.tanh()
        else:
            y = y.view(x.shape[0], -1).tanh()
        x = torch.cat((x, y), dim=1)
        y = x.view(x.shape[0], -1).tanh()
        y = torch.cat((y, y), dim=-2)
        x = x.view(-1)
        return y



func = Model().to('cpu')


x = torch.randn(1, 3, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 3 and 2

jit:
Failed running call_function <built-in method cat of type object at 0x7bb974996ec0>(*((FakeTensor(..., size=(1, 3, 2)), FakeTensor(..., size=(1, 6))),), **{'dim': 1}):
Number of dimensions of tensors must match.  Expected 3-D tensors, but got 2-D for tensor number 1 in the list

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''