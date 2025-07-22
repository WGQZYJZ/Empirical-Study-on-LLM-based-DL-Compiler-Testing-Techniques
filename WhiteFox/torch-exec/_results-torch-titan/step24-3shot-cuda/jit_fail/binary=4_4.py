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
        self.__linear__ = torch.nn.Linear(3, 8)

    def forward(self, input, x):
        y = self.__linear__(input)
        z = (y + x)
        return z



func = Model().to('cuda')



input = torch.randn(1, 3, 32, 32)



__other__ = torch.randn(1, 8, 32, 32)


test_inputs = [input, __other__]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (96x32 and 3x8)

jit:
Failed running call_module L__self_____linear__(*(FakeTensor(..., device='cuda:0', size=(1, 3, 32, 32)),), **{}):
a and b must have same reduction dim, but got [96, 32] X [3, 8].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''