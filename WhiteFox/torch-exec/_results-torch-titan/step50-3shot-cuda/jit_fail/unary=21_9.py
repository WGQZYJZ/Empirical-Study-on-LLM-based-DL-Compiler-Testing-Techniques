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
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 24, 1, stride=1)
        self.conv2 = torch.nn.Conv2d(24, 100, 1, stride=1)
        self.conv3 = torch.nn.Conv2d(100, 64, 1, stride=1)
        self.conv4 = torch.nn.Conv2d(64, 1, 3, stride=1, padding=1)
        self.hardtanh_1 = torch.nn.Hardtanh()
        self.hardtanh_2 = torch.nn.Hardtanh()
        self.tanh = torch.nn.Tanh()
        self.flatten = torch.nn.Flatten(1, (- 1))
        self.linear1 = torch.nn.Linear(200, 300)
        self.linear2 = torch.nn.Linear(300, 1)

    def forward(self, x97):
        x96 = self.conv1(x97)
        x19 = self.conv2(x96)
        x3 = self.conv3(x19)
        x9 = self.conv4(x3)
        x10 = self.hardtanh_1(x9)
        x11 = self.hardtanh_2(x10)
        x12 = self.hardtanh_2(x11)
        x13 = self.hardtanh_1(x12)
        x14 = self.hardtanh_1(x3)
        x15 = self.hardtanh_1(x14)
        x16 = self.hardtanh_2(x15)
        x5 = self.tanh(x16)
        x32 = self.flatten(x5)
        x33 = self.linear1(x32)
        x95 = self.tanh(x33)
        x98 = self.tanh(x95)
        x119 = self.linear2(x98)
        return x119




func = ModelTanh().to('cuda')



x97 = torch.randn(4, 3, 224, 224)


test_inputs = [x97]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x3211264 and 200x300)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(4, 3211264)),), **{}):
a and b must have same reduction dim, but got [4, 3211264] X [200, 300].

from user code:
   File "<string>", line 44, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''