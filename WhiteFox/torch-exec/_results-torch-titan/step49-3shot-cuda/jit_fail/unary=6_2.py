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
        self.conv = torch.nn.Conv2d(3, 64, 3, stride=1, padding=1)
        self.flatten = torch.nn.Flatten(1, 3)
        self.linear = torch.nn.Linear(5408, 256)
        self.avgpool = torch.nn.AvgPool2d(kernel_size=1)
        self.fc = torch.nn.Linear(256, 1)

    def forward(self, x1):
        t1 = self.linear(self.flatten(self.conv(x1)))
        t2 = self.avgpool(t1)
        t3 = self.fc(torch.flatten(t2, 1))
        return t3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x65536 and 5408x256)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 65536)),), **{}):
a and b must have same reduction dim, but got [1, 65536] X [5408, 256].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''