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
        self.conv1 = torch.nn.Conv2d(3, 32, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(32, 64, 3, stride=1, padding=1)

    def forward(self, x1):
        t1 = self.conv1(x1)
        t2 = self.conv2(t1)
        (t3, _) = torch.max(t2, dim=-1)
        t4 = torch.cat([t1, t3], dim=1)
        return t4


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 4 and 3

jit:
Failed running call_function <built-in method cat of type object at 0x7cf2b8396ec0>(*([FakeTensor(..., size=(1, 32, 64, 64)), FakeTensor(..., size=(1, 64, 64))],), **{'dim': 1}):
Number of dimensions of tensors must match.  Expected 4-D tensors, but got 3-D for tensor number 1 in the list

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''