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
        self.linear = torch.nn.Linear(2, 8, bias=False)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.randn(8)
        v3 = (v1 + v2)
        v4 = torch.relu(v3)
        return v4



func = Model().to('cuda')



x1 = torch.randn(67108864)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x67108864 and 2x8)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(67108864,)),), **{}):
a and b must have same reduction dim, but got [1, 67108864] X [2, 8].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''