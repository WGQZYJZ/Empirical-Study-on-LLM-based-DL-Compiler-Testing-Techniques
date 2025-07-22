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
        self.flatten = torch.nn.Flatten(start_dim=1)
        self.linear_1 = torch.nn.Linear(45, 9)

    def forward(self, x1):
        v1 = self.flatten(x1)
        v2 = self.linear_1(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x3072 and 45x9)

jit:
Failed running call_module L__self___linear_1(*(FakeTensor(..., device='cuda:0', size=(1, 3072)),), **{}):
a and b must have same reduction dim, but got [1, 3072] X [45, 9].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''