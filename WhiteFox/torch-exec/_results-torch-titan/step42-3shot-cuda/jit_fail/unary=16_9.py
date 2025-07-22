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
        self.linear = torch.nn.Linear(4, 2)

    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = torch.relu(v1)
        return v2



func = Model().to('cuda')



x2 = torch.randn(2, 1, 2, 3)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x3 and 4x2)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(2, 1, 2, 3)),), **{}):
a and b must have same reduction dim, but got [4, 3] X [4, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''