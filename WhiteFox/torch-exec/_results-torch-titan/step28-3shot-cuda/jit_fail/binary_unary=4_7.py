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
        self.linear = torch.nn.Linear(10, 20)

    def forward(self, x2, other):
        v1 = self.linear(x2)
        v2 = (v1 + other)
        v3 = torch.relu(v2)
        return v3



func = Model().to('cuda')



other = torch.randn(20, 500)



x2 = torch.randn(10, 500)


test_inputs = [other, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x500 and 10x20)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(20, 500)),), **{}):
a and b must have same reduction dim, but got [20, 500] X [10, 20].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''