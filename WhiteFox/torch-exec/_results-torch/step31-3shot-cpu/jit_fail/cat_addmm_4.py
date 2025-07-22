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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.cat = torch.cat

    def forward(self, x):
        x = x.flatten(1)
        return self.cat((x, x.t()), dim=1)



func = Model().to('cpu')


x = torch.randn(3, 5)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 3 but got size 5 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x73eaeed96ec0>(*((FakeTensor(..., size=(s0, s1)), FakeTensor(..., size=(s1, s0))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected s0 in dimension 0 but got s1 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''