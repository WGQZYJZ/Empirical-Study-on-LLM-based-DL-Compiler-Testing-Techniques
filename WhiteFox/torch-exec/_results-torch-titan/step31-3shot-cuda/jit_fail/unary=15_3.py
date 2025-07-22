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
        self.fc1 = torch.nn.Linear(((3 * 28) * 28), 320)
        self.fc2 = torch.nn.Linear(320, 10)

    def forward(self, x1):
        v1 = x1.view((- 1), 3, 28, 28)
        v2 = self.fc1(v1)
        v3 = self.fc2(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(8, 3, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (672x28 and 2352x320)

jit:
Failed running call_module L__self___fc1(*(FakeTensor(..., device='cuda:0', size=(8, 3, 28, 28)),), **{}):
a and b must have same reduction dim, but got [672, 28] X [2352, 320].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''