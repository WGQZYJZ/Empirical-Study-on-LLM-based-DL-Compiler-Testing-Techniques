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
        self.f0 = torch.nn.Linear(5, 6)

    def forward(self, x1, x2):
        t1 = torch.cat([torch.mm(x1, x2), torch.mm(x1, x2)], 1)
        t2 = self.f0(t1)
        t3 = self.f0(t1)
        return torch.cat([t2, t3], 1)




func = Model().to('cuda')



x1 = torch.randn(3, 5)



x2 = torch.randn(5, 1)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x2 and 5x6)

jit:
Failed running call_module L__self___f0(*(FakeTensor(..., device='cuda:0', size=(3, 2)),), **{}):
a and b must have same reduction dim, but got [3, 2] X [5, 6].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''