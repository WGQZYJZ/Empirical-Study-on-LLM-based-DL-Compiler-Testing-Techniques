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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super(ModelTanh, self).__init__()
        self.conv = torch.nn.Conv2d(3, 1, 3)
        self.relu = torch.nn.ReLU()
        self.max_pool = torch.nn.MaxPool2d(3, 2)
        self.tanh = torch.nn.Tanh()
        self.avg_pool = torch.nn.AvgPool2d(3, 2)
        self.flatten = torch.nn.Flatten()
        self.linear = torch.nn.Linear(225, 1010)
        self.relu_a = torch.nn.ReLU()
        self.linear_1 = torch.nn.Linear(1010, 410)
        self.relu_b = torch.nn.ReLU()
        self.linear_e = torch.nn.Linear(410, 26250)

    def forward(self, x):
        r1 = self.conv(x)
        r2 = self.relu(r1)
        r3 = self.max_pool(r2)
        r4 = self.tanh(r3)
        r5 = self.avg_pool(x)
        r6 = self.flatten(r4)
        r7 = self.linear(r5)
        r8 = self.relu_a(r7)
        r9 = self.linear_1(r8)
        r10 = self.relu_b(r9)
        r11 = self.linear_e(r10)
        return r11




func = ModelTanh().to('cuda')



x1 = torch.randn(1, 3, 32, 34)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (45x16 and 225x1010)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 3, 15, 16)),), **{}):
a and b must have same reduction dim, but got [45, 16] X [225, 1010].

from user code:
   File "<string>", line 38, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''