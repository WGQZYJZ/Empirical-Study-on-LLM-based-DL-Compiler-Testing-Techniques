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
        self.linear1 = torch.nn.Linear(1, 2)
        self.linear2 = torch.nn.Linear(2, 2)
        self.linear3 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v0 = self.linear1(x1)
        v1 = torch.nn.functional.linear(x1, self.linear2.weight, self.linear2.bias)
        v2 = v1.permute(0, 2, 1)
        v3 = (x1 - v2)
        v4 = (v0 + v3)
        v5 = torch.nn.functional.linear(v4, self.linear3.weight, self.linear3.bias)
        v6 = (x1 + v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 1, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2 and 1x2)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(1, 1, 2)),), **{}):
a and b must have same reduction dim, but got [1, 2] X [1, 2].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''