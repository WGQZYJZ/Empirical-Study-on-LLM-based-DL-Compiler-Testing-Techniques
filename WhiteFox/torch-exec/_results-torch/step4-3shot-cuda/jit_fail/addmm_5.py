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
        v2 = v1 + inp
        return v2



func = Model().to('cuda')


x1 = torch.randn(12, 666)

x2 = torch.randn(6, 666)

inp = torch.randn(6, 12)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
The size of tensor a (666) must match the size of tensor b (12) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(s2, s1)), FakeTensor(..., device='cuda:0', size=(s2, s0))), **{}):
The size of tensor a (s1) must match the size of tensor b (s0) at non-singleton dimension 1)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''