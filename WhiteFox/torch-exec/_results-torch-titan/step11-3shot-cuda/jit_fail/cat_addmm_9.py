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



class FC(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.weight = torch.randn((128, 25, 1, 1))
        self.bias = torch.randn(128)

    def forward(self, x):
        dim = 1
        t1 = torch.addmm(self.bias, x, self.weight.squeeze())
        t2 = torch.cat([t1], dim)
        return t2



func = FC().to('cuda')



x = torch.randn(300, 128, 16)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 must be a matrix, got 3-D tensor

jit:
Failed running call_function <built-in method addmm of type object at 0x7560e48699e0>(*(FakeTensor(..., device='cuda:0', size=(128,)), FakeTensor(..., device='cuda:0', size=(300, 128, 16)), FakeTensor(..., device='cuda:0', size=(128, 25))), **{}):
a must be 2D

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''