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
        from torch import nn
        super().__init__()
        self.linear = nn.Linear(100, 10)
        self.maxpool = nn.MaxPool2d(2, 2)

    def forward(self, x1):
        l1 = self.linear(x1)
        mx = self.maxpool(l1)
        l2 = mx.clamp(min=0, max=6)
        l3 = (l2 / 6)
        return l3



func = Model().to('cuda')



x1 = torch.randn(1, 100, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2800x28 and 100x10)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 100, 28, 28)),), **{}):
a and b must have same reduction dim, but got [2800, 28] X [100, 10].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''