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
        self.linear = torch.nn.Linear(16, 1, bias=False)
        self.linear.weight = torch.nn.Parameter((torch.eye(16, 1) * 0.1))

    def forward(self, x1):
        t1 = self.linear(x1)
        t2 = (t1 + x1)
        t3 = torch.relu(t2)
        return t3



func = Model().to('cuda')



x1 = torch.randn(8, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x16 and 1x16)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(8, 16)),), **{}):
a and b must have same reduction dim, but got [8, 16] X [1, 16].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''