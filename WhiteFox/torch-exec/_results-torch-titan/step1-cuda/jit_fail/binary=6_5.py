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
        self.linear = torch.nn.Linear(28, 30)

    def forward(self, x, other):
        v1 = self.linear(x)
        v2 = (v1 - other)
        return v2



func = Model().to('cuda')



x = torch.randn(1, 3, 3)



other = torch.randn(1, 4, 5)


test_inputs = [x, other]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x3 and 28x30)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 3, 3)),), **{}):
a and b must have same reduction dim, but got [3, 3] X [28, 30].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''