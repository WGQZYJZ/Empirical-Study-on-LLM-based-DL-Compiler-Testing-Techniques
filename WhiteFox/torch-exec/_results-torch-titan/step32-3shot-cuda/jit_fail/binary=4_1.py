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
        self.linear1 = torch.nn.Linear(10, 256)

    def forward(self, x, other):
        v1 = self.linear1(x)
        v2 = (v1 + other)
        return v2



func = Model().to('cuda')



other = torch.tensor([[1.0, 2.0]])



x = torch.randn(1, 10)


test_inputs = [other, x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2 and 10x256)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(1, 2)),), **{}):
a and b must have same reduction dim, but got [1, 2] X [10, 256].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''