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
        self.linear = torch.nn.Linear(10, 3)

    def forward(self, inputs):
        v1 = self.linear(inputs)
        v2 = (v1 + other)
        return v2



func = Model().to('cuda')



inputs = torch.randn(1, 4, 4)


test_inputs = [inputs]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x4 and 10x3)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 4, 4)),), **{}):
a and b must have same reduction dim, but got [4, 4] X [10, 3].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''