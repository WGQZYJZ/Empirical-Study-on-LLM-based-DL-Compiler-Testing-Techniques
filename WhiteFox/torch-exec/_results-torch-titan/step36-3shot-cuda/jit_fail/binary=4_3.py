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

    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(1584, 43, bias=False)
        self.other = torch.tensor(other, requires_grad=False)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + self.other)
        return v2



other = 1
func = Model(torch.rand(43)).to('cuda')



x1 = torch.randn(5, 43)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x43 and 1584x43)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(5, 43)),), **{}):
a and b must have same reduction dim, but got [5, 43] X [1584, 43].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''