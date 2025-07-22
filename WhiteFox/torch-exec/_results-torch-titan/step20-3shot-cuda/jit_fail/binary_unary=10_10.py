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
        self.linear = torch.nn.Linear(((64 * 64) * 3), 10)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = (v1 + x2)
        v3 = torch.nn.functional.relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(64, 64, 3)



x2 = torch.randn(64, 64, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4096x3 and 12288x10)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(64, 64, 3)),), **{}):
a and b must have same reduction dim, but got [4096, 3] X [12288, 10].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''