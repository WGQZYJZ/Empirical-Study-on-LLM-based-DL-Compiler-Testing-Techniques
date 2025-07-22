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
        self.upsample = torch.nn.Upsample(scale_factor=2, mode='nearest')
        self.linear_1 = torch.nn.Linear(5, 20)
        self.linear_2 = torch.nn.Linear(20, 10)

    def forward(self, x1):
        v1 = torch.relu(x1)
        v2 = torch.cat([x1, (2 * v1)], 1)
        v3 = self.linear_1(v2)
        v4 = self.linear_2(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x10 and 5x20)

jit:
Failed running call_module L__self___linear_1(*(FakeTensor(..., device='cuda:0', size=(1, 10)),), **{}):
a and b must have same reduction dim, but got [1, 10] X [5, 20].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''