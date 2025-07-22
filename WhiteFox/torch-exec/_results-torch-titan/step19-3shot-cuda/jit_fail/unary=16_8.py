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
        self.linear1 = torch.nn.Linear(784, 64)
        self.linear2 = torch.nn.Linear(64, 32)
        self.linear3 = torch.nn.Linear(32, 16)
        self.linear4 = torch.nn.Linear(16, 8)
        self.linear5 = torch.nn.Linear(8, 4)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = self.linear2(v1)
        v3 = self.linear3(v2)
        v4 = self.linear4(v3)
        v5 = self.linear5(v4)
        return v5



func = Model().to('cuda')



x1 = torch.rand(64, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12288x64 and 784x64)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(64, 3, 64, 64)),), **{}):
a and b must have same reduction dim, but got [12288, 64] X [784, 64].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''