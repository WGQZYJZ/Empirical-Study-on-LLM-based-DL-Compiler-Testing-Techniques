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

    def forward(self, x, y):
        (A, B, C, D) = torch.chunk(x, 4, dim=(- 1))
        E = torch.relu((((A + B) + C) + D))
        (a, b, c) = torch.chunk(E, 3, dim=1)
        F = ((a + b) + c)
        return F




func = Model().to('cuda')



x = torch.randn(64, 128, 64)



y = torch.randn(64, 128, 32)


test_inputs = [x, y]

# JIT_FAIL
'''
direct:
The size of tensor a (43) must match the size of tensor b (42) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(64, 43, 16)), FakeTensor(..., device='cuda:0', size=(64, 42, 16))), **{}):
Attempting to broadcast a dimension of length 42 at -2! Mismatching argument at index 1 had torch.Size([64, 42, 16]); but expected shape should be broadcastable to [64, 43, 16]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''