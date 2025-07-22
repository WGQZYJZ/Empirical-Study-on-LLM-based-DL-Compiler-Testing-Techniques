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
        y = torch.cat([x[:1], x], dim=1)
        y = y.view(y.shape[0], -1)
        y = y.tanh()
        y = torch.cat([y, y], dim=1)
        x = y.tanh()
        return x



func = Model().to('cpu')


x = torch.randn(2, 3, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 1 but got size 2 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x764fe8596ec0>(*([FakeTensor(..., size=(1, 3, 4)), FakeTensor(..., size=(s0, 3, 4))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 1 in dimension 0 but got s0 for tensor number 1 in the list

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''