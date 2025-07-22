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
        super(Model, self).__init__()
        self.conv1 = torch.nn.Conv2d(2, 4, 3)
        self.conv2 = torch.nn.Conv2d(4, 8, 5)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        t1 = torch.cat((v2, v1), 1)
        w1 = torch.transpose(t1, 2, 3)
        w2 = torch.transpose(w1, 1, 2)
        w3 = w2.contiguous()
        w4 = torch.transpose(w3, 2, 3)
        w5 = torch.transpose(w4, 1, 2)
        w6 = w5.reshape((-1, 4, 16))
        return w6



func = Model().to('cpu')


x1 = torch.randn(4, 2, 10, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 4 but got size 8 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x771bf9b96ec0>(*((FakeTensor(..., size=(4, 8, 4, 4)), FakeTensor(..., size=(4, 4, 8, 8))), 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 4 in dimension 2 but got 8 for tensor number 1 in the list

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''