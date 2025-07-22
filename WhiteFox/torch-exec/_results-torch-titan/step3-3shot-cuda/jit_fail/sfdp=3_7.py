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
        self.mat1 = torch.nn.Linear(512, 512)
        self.mat2 = torch.nn.Linear(512, 512)
        self.mat3 = torch.nn.Linear(512, 512)
        self.mat5 = torch.nn.Linear(512, 512)
        self.mat6 = torch.nn.Linear(512, 512)

    def forward(self, xin1):
        xout1 = self.mat1(xin1)
        xout2 = self.mat2(xout1)
        qk = xout1.matmul(xout2.transpose((- 2), (- 1)))
        qk2 = self.mat3(qk)
        qk3 = self.mat5(qk2)
        qk4 = self.mat6(qk3)
        vout = xout2.matmul(qk4)
        return vout



func = Model().to('cuda')



xin1 = torch.randn(1, 512)


test_inputs = [xin1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1 and 512x512)

jit:
Failed running call_module L__self___mat3(*(FakeTensor(..., device='cuda:0', size=(1, 1)),), **{}):
a and b must have same reduction dim, but got [1, 1] X [512, 512].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''