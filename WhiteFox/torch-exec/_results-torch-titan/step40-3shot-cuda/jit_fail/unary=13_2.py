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
        self.linear1 = torch.nn.Linear(64, 32, bias=True)
        self.linear2 = torch.nn.Linear(32, 64, bias=True)

    def forward(self, q1):
        y1 = self.linear1(q1)
        y2 = torch.sigmoid(y1)
        y3 = (y1 * y2)
        output = self.linear2(y3)
        return output



func = Model().to('cuda')



q1 = torch.randn(1, 64, 1)


test_inputs = [q1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (64x1 and 64x32)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(1, 64, 1)),), **{}):
a and b must have same reduction dim, but got [64, 1] X [64, 32].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''