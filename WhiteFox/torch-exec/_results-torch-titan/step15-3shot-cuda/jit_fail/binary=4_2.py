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
        self.linear_1 = torch.nn.Linear(10, 10)
        self.linear_2 = torch.nn.Linear(10, 1)

    def forward(self, x1):
        v1 = self.linear_1(x1)
        v2 = self.linear_2(v1)
        return (v2 + other)



func = Model().to('cuda')



x1 = torch.randn(1, 10, 16, 17)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (160x17 and 10x10)

jit:
Failed running call_module L__self___linear_1(*(FakeTensor(..., device='cuda:0', size=(1, 10, 16, 17)),), **{}):
a and b must have same reduction dim, but got [160, 17] X [10, 10].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''