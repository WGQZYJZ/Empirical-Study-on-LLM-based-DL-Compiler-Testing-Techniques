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
        self.linear = torch.nn.Linear(8, 64, bias=True)

    def forward(self, x2):
        y1 = self.linear(x2)
        y2 = (y1 * torch.clamp((y1 + 3), min=0, max=6))
        y3 = (y2 / 6)
        return y3



func = Model().to('cuda')



x2 = torch.randn(1, 64, 28, 28)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1792x28 and 8x64)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 64, 28, 28)),), **{}):
a and b must have same reduction dim, but got [1792, 28] X [8, 64].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''