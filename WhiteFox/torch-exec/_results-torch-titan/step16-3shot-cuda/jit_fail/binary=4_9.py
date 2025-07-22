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
        self.linear = torch.nn.Linear(8, 6)

    def forward(self, x1, x2):
        v4 = self.linear(torch.cat((x1, x2), dim=1))
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 8)



x2 = torch.randn(1, 8)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x16 and 8x6)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 16)),), **{}):
a and b must have same reduction dim, but got [1, 16] X [8, 6].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''