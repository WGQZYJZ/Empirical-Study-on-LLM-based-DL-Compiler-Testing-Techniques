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

    def __init__(self, n):
        super().__init__()
        self.linear = torch.nn.Linear(8, n)

    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = (v1 + other)
        return v2




n = 10

func = Model(n).to('cuda')



n = 10


x1 = torch.randn(1, n)



n = 10


other = torch.randn(1, n)


test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x10 and 8x10)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 10)),), **{}):
a and b must have same reduction dim, but got [1, 10] X [8, 10].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''