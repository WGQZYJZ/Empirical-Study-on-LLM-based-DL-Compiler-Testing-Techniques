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

    def __init__(self, neg_slope):
        super().__init__()
        self.fc = torch.nn.Linear(8, 256)
        self.neg_slope = neg_slope

    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = v1.shape[(- 1)]
        t1 = v1.reshape([(- 1), v2])
        v3 = (t1 > 0)
        v6 = v1.shape[(- 1)]
        t2 = v3.reshape([(- 1), v6])
        v4 = (t1 * self.neg_slope)
        v5 = torch.where(t2, v1, v4)
        t3 = v5.reshape([(- 1), 8, 32, 32])
        return t3



neg_slope = 1
func = Model(0.1).to('cuda')



x1 = torch.randn(1, 8, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (256x32 and 8x256)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32)),), **{}):
a and b must have same reduction dim, but got [256, 32] X [8, 256].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''