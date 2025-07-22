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

    def forward(self, x1):
        l1 = self.linear(x1)
        l2 = (l1 * torch.clamp(torch.clamp((l1 + 3), 0, 6), 0, 6))
        l3 = (l2 / 6)
        return l3



func = Model().to('cuda')



x1 = torch.randn(1, 7)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x7 and 8x6)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 7)),), **{}):
a and b must have same reduction dim, but got [1, 7] X [8, 6].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''