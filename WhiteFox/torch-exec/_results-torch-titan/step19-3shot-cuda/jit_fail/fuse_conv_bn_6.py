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
        self.conv = torch.nn.Conv2d(2, 2, 2)
        self.bn = torch.nn.BatchNorm1d(2)
        self.linear_relu = torch.nn.Sequential(torch.nn.Linear(2, 3), torch.nn.ReLU())

    def forward(self, x):
        y = self.conv(x)
        y = self.linear_relu(y)
        z = self.bn(y)
        return t.sum(z)




func = Model().to('cuda')



x = torch.randn(1, 2, 4, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x3 and 2x3)

jit:
Failed running call_module L__self___linear_relu_0(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3, 3)),), **{}):
a and b must have same reduction dim, but got [6, 3] X [2, 3].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''