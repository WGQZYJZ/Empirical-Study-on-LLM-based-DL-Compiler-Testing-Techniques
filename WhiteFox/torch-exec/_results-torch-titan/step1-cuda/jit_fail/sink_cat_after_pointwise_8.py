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

    def __init__(self, n):
        super().__init__()
        self.l1 = torch.nn.Linear(1, n)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        y1 = self.l1(x)
        y2 = self.relu(y1)
        y3 = self.l1(y2)
        y4 = torch.cat((y1, y2))
        y5 = torch.tanh(y4)
        return y5




n = 2

func = Model(n).to('cuda')



x = torch.randn(1, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2 and 1x2)

jit:
Failed running call_module L__self___l1(*(FakeTensor(..., device='cuda:0', size=(1, 2)),), **{}):
a and b must have same reduction dim, but got [1, 2] X [1, 2].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''