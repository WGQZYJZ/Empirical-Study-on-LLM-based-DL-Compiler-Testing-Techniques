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
        self.conv = torch.nn.Sequential(torch.nn.Conv2d(16, 32, 3, stride=1, padding=1), torch.nn.Conv2d(32, 32, 3, stride=1, padding=1), torch.nn.Conv2d(32, 32, 3, stride=1, padding=1), torch.nn.Conv2d(32, 32, 3, stride=1, padding=1), torch.nn.Conv2d(32, 32, 3, stride=1, padding=1))
        self.lin = torch.nn.Linear(32, 2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1[:, (- 1), :, :]
        v3 = (v2 - 0.2)
        v4 = F.relu(v3)
        v5 = self.lin(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 16, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x16 and 32x2)

jit:
Failed running call_module L__self___lin(*(FakeTensor(..., device='cuda:0', size=(1, 16, 16)),), **{}):
a and b must have same reduction dim, but got [16, 16] X [32, 2].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''