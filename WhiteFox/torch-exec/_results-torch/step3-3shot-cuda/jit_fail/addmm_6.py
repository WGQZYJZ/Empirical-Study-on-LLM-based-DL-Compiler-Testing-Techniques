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

    def forward(self, x1, x2, inp):
        v1 = torch.mm(inp, x1)
        v2 = v1 + x2
        return v2



func = Model().to('cuda')


x1 = torch.randn(12, 6)

x2 = torch.randn(6, 6)

inp = torch.randn(12, 6)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x6 and 12x6)

jit:
Failed running call_function <built-in method mm of type object at 0x7db545996ec0>(*(FakeTensor(..., device='cuda:0', size=(s2, s3)), FakeTensor(..., device='cuda:0', size=(s0, s1))), **{}):
a and b must have same reduction dim, but got [s2, s3] X [s0, s1].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''