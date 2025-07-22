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
        self.Linear = torch.nn.Linear(16, 8)
        self.other = torch.nn.Linear(16, 8)

    def forward(self, x1):
        x1 = self.Linear(x1)
        x2 = self.other(x1)
        return x2



func = Model().to('cuda')



x1 = torch.randn(1, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x8 and 16x8)

jit:
Failed running call_module L__self___other(*(FakeTensor(..., device='cuda:0', size=(1, 8)),), **{}):
a and b must have same reduction dim, but got [1, 8] X [16, 8].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''