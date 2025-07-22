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
        self.l5 = torch.nn.Linear(10, 20, bias=False)

    def forward(self, x1):
        l1 = x1.mean(dim=[(- 1)], keepdims=True)
        l2 = self.l5(l1)
        l3 = (l2 + 3)
        l4 = torch.clamp_min(l3, 0)
        l5 = torch.clamp_max(l4, 6)
        return l5



func = Model().to('cuda')



x1 = torch.randn(32, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (32x1 and 10x20)

jit:
Failed running call_module L__self___l5(*(FakeTensor(..., device='cuda:0', size=(32, 1)),), **{}):
a and b must have same reduction dim, but got [32, 1] X [10, 20].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''