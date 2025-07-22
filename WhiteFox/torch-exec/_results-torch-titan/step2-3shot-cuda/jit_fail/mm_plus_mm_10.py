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
        self.fc1 = torch.nn.Linear(1, 1)
        self.out = torch.nn.Linear(1, 1)

    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = (v1 + v2)
        v4 = self.fc1(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 65)



x2 = torch.randn(65, 5)



x3 = torch.randn(1, 65)



x4 = torch.randn(65, 5)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x5 and 1x1)

jit:
Failed running call_module L__self___fc1(*(FakeTensor(..., device='cuda:0', size=(1, 5)),), **{}):
a and b must have same reduction dim, but got [1, 5] X [1, 1].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''