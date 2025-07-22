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
        self.fc = torch.nn.Linear(5, 6)
        self.fc2 = torch.nn.Linear(5, 6)

    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = self.fc2(x1)
        v3 = torch.addmm(v2, v1, v2)
        v4[:, :, 1, 1:] = v3
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 5, 128, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (640x16 and 5x6)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(1, 5, 128, 16)),), **{}):
a and b must have same reduction dim, but got [640, 16] X [5, 6].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''