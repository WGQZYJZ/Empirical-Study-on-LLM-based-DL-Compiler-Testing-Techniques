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
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 1)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = torch.tanh(v1)
        y = self.linear2(v2)
        return y



func = Model().to('cuda')



x1 = torch.randn(1, 2, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (128x64 and 2x4)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(1, 2, 64, 64)),), **{}):
a and b must have same reduction dim, but got [128, 64] X [2, 4].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''