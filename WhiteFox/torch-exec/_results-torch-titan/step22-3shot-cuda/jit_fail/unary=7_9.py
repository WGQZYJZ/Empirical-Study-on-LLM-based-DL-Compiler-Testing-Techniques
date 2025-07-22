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
        self.linear = torch.nn.Linear(8, 128)

    def forward(self, x1):
        y1 = self.linear(x1)
        y2 = (y1 * torch.clamp((y1 + 3), min=0, max=6))
        y3 = (y2 / 6)
        return y3



func = Model().to('cuda')



x1 = torch.randn(8, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x128 and 8x128)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(8, 128)),), **{}):
a and b must have same reduction dim, but got [8, 128] X [8, 128].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''