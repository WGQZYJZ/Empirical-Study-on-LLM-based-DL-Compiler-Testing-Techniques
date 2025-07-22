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
        self.linear = torch.nn.Linear(14, 10)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        return v6



func = Model().to('cuda')



x1 = torch.randn(20, 14, 1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (280x1 and 14x10)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(20, 14, 1, 1)),), **{}):
a and b must have same reduction dim, but got [280, 1] X [14, 10].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''