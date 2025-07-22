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
        self.linear = torch.nn.Linear(3, 6)

    def forward(self, x):
        z = torch.cat((x, self.linear(x)), dim=1)
        w = torch.tanh(z)
        v = torch.relu(w)
        return v




func = Model().to('cuda')



x = torch.randn(5, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (15x4 and 3x6)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(5, 3, 4)),), **{}):
a and b must have same reduction dim, but got [15, 4] X [3, 6].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''