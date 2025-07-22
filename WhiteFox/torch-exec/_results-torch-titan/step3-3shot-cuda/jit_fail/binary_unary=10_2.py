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
        self.pre_linear = torch.nn.Sequential(torch.nn.Conv2d(3, 6, 1, stride=1, padding=1), torch.nn.ReLU(), torch.nn.Conv2d(6, 9, 3, stride=1, padding=1), torch.nn.ReLU(), torch.nn.MaxPool2d(2))
        self.linear = torch.nn.Linear(180, 10)

    def forward(self, x1):
        v1 = self.pre_linear(x1)
        v3 = torch.flatten(v1, 1)
        v4 = self.linear(v3)
        return v4




class Model1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 14)

    def forward(self, x1):
        v1 = self.linear(x1)
        return v1



func = Model1().to('cuda')



x1 = torch.randn(1, 3, 96, 96)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (288x96 and 32x14)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 3, 96, 96)),), **{}):
a and b must have same reduction dim, but got [288, 96] X [32, 14].

from user code:
   File "<string>", line 38, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''