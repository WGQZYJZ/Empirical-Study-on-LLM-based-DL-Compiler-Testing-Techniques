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
        self.linear_layer = torch.nn.Linear(2, 8)

    def forward(self, x1):
        v1 = self.linear_layer(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 2, 3, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x4 and 2x8)

jit:
Failed running call_module L__self___linear_layer(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3, 4)),), **{}):
a and b must have same reduction dim, but got [6, 4] X [2, 8].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''