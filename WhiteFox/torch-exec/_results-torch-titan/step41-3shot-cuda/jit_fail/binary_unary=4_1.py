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
        self.linear1 = torch.nn.Linear(3, 5)
        self.linear2 = torch.nn.Linear(5, 6)

    def forward(self, x1, other):
        v1 = self.linear1(x1)
        v2 = (v1 + other)
        v3 = torch.nn.functional.relu(v2)
        v4 = self.linear2(v3)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)



other = torch.randn(1, 5)


test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (672x224 and 3x5)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 224, 224)),), **{}):
a and b must have same reduction dim, but got [672, 224] X [3, 5].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''