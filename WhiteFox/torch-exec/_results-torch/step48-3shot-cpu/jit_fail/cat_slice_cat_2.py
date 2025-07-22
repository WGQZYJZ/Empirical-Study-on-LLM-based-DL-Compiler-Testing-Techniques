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

    def __init__(self, size):
        super().__init__()
        self.size = size

    def forward(self, *args):
        n = len(args) // 2
        l1 = args[:n]
        l2 = args[n:]
        t1 = torch.cat(l1, dim=1)
        t3 = t1[:, :, self.size:]
        t4 = torch.cat((t1, t3), dim=1)
        return t4


size = 13
func = Model(size).to('cpu')


x1 = torch.randn(1, 1, 64, 52)

x2 = torch.randn(1, 1, 64, 34)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 64 but got size 51 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x799debf96ec0>(*((FakeTensor(..., size=(1, 1, 64, 52)), FakeTensor(..., size=(1, 1, 51, 52))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 64 in dimension 2 but got 51 for tensor number 1 in the list

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''