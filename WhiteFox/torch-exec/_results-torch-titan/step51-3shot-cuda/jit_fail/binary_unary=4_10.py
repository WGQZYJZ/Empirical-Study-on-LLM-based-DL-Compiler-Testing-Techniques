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
        self.linear = torch.nn.Linear(2, 70, bias=True)

    def forward(self, x1, other):
        t1 = self.linear(x1)
        t2 = (t1 + other)
        t3 = torch.nn.functional.relu(t2)
        return t3



func = Model().to('cuda')



other = torch.rand(70)



x1 = torch.randn(1, 2)


test_inputs = [other, x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x70 and 2x70)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(70,)),), **{}):
a and b must have same reduction dim, but got [1, 70] X [2, 70].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''