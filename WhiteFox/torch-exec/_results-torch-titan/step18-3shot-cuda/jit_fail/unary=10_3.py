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
        self.linear = torch.nn.Linear(1, 2)

    def forward(self, x1):
        t1 = self.linear(x1)
        t2 = (t1 + 3)
        t3 = torch.clamp_min(t2, 0)
        t4 = torch.clamp_max(t3, 6)
        t5 = (t4 / 6)
        return t5



func = Model().to('cuda')



x1 = torch.randn(2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2 and 1x2)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(2,)),), **{}):
a and b must have same reduction dim, but got [1, 2] X [1, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''