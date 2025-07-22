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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        x2 = torch.unsqueeze(x1, dim=(- 1))
        v1 = self.linear(x2).clamp(min=0)
        x3 = torch.squeeze(v1, dim=(- 1))
        return torch.min(x3, dim=(- 1))[1]




func = Model().to('cuda')



x1 = torch.randn(1, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x1 and 2x2)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 2, 1)),), **{}):
a and b must have same reduction dim, but got [2, 1] X [2, 2].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''