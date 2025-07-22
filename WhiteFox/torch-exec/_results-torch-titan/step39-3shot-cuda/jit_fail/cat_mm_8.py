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
        self.m = torch.nn.Linear(2, 2)
        self.l = ([self.m] * 10)

    def forward(self, x1, x2):
        v = [torch.mm(self.m((x1 * x2)), self.m((x1 * x2))) for loopVar1 in range(10)]
        return torch.cat(v, 1)




func = Model().to('cuda')



x1 = torch.randn(12, 6)



x2 = torch.randn(12, 6)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x6 and 2x2)

jit:
Failed running call_module L__self___m(*(FakeTensor(..., device='cuda:0', size=(12, 6)),), **{}):
a and b must have same reduction dim, but got [12, 6] X [2, 2].

from user code:
   File "<string>", line 23, in forward
  File "<string>", line 23, in <listcomp>


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''