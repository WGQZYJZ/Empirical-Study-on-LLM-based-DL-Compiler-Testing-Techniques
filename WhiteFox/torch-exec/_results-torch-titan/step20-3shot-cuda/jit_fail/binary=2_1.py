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
        self.conv = torch.nn.Conv2d(5, 8, 1, stride=1, padding=1)
        self.dense = torch.nn.Linear(16, 8)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.flatten(v1, (- 1))
        v3 = self.dense(v2)
        v4 = torch.flatten(v3, 0)
        v5 = (v4 - torch.tensor([0.59, 0.55, 0.94, 0.37, 0.63]))
        return v5




func = Model().to('cuda')



x = torch.randn(1, 5, 32, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (272x66 and 16x8)

jit:
Failed running call_module L__self___dense(*(FakeTensor(..., device='cuda:0', size=(1, 8, 34, 66)),), **{}):
a and b must have same reduction dim, but got [272, 66] X [16, 8].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''