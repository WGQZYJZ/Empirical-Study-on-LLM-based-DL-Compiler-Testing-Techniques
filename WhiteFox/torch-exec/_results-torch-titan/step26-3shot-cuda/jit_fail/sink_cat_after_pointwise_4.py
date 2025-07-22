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
        self.m1 = torch.nn.Linear(1, 2)
        self.m2 = torch.nn.Linear(10, 10)

    def forward(self, x):
        x = torch.cat([x, x], dim=1)
        x = torch.relu((x + self.m1(x)))
        return self.m2(x)




func = Model().to('cuda')



x = torch.randn(3, 2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x2 and 1x2)

jit:
Failed running call_module L__self___m1(*(FakeTensor(..., device='cuda:0', size=(3, 4, 2)),), **{}):
a and b must have same reduction dim, but got [12, 2] X [1, 2].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''