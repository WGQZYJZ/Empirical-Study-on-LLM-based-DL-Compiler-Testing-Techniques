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
        self.linear = torch.nn.Linear(1024, 10)
        self.bn = torch.nn.BatchNorm2d(1024)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = self.bn(v1)
        v3 = torch.relu(v2)
        return v3



func = Model().to('cuda')



x = torch.randn(1, 1024, 1, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1024x1 and 1024x10)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 1024, 1, 1)),), **{}):
a and b must have same reduction dim, but got [1024, 1] X [1024, 10].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''