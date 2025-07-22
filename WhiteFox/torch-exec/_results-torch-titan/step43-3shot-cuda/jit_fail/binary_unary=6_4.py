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
        self.linear = torch.nn.Linear(1, 1, bias=False)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 - (- 1.714285766124735))
        v3 = torch.relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x64 and 1x1)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(64,)),), **{}):
a and b must have same reduction dim, but got [1, 64] X [1, 1].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''