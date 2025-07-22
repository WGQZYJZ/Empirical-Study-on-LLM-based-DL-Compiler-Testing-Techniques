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
        self.conv = torch.nn.Conv2d(2, 2, 2, bias=False)
        self.bn = torch.nn.BatchNorm2d(2)

    def forward(self, input_tensor):
        return torch.cat((self.conv(input_tensor), self.bn(input_tensor)), dim=1)



func = Model().to('cpu')


x = torch.randn(1, 2, 5, 5)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 4 but got size 5 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x72741f196ec0>(*((FakeTensor(..., size=(1, 2, 4, 4)), FakeTensor(..., size=(1, 2, 5, 5))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 4 in dimension 2 but got 5 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''