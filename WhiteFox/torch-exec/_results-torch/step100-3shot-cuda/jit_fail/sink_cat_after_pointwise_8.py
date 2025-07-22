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

    def __init__(self, n0: int, n1: int):
        super().__init__()
        self.weight0 = torch.randn(n0, n1)
        self.weight1 = torch.randn(n1, n0)

    def forward(self, x):
        y = self.weight0.matmul(x)
        y = y.softmax(dim=1)
        y = y.matmul(self.weight1)
        y = y.sigmoid()
        return y


n0 = 1
n1 = 1

func = Model(n0, n1).to('cuda')


x = torch.randn(5, 3)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1 and 5x3)

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 1)), FakeTensor(..., device='cuda:0', size=(s0, s1))), **{}):
a and b must have same reduction dim, but got [1, 1] X [s0, s1].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''