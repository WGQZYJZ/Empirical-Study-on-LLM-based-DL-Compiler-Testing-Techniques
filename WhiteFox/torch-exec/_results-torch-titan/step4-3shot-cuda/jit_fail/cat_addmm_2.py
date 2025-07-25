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
        self.fc1 = torch.nn.Linear(10, 20)
        self.fc2 = torch.nn.Linear(30, 40)

    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = torch.cat([v1], dim=1)
        v3 = self.fc2(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x20 and 30x40)

jit:
Failed running call_module L__self___fc2(*(FakeTensor(..., device='cuda:0', size=(1, 20)),), **{}):
a and b must have same reduction dim, but got [1, 20] X [30, 40].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''