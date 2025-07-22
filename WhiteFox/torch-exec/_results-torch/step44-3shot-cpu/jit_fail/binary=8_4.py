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
        self.conv1 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.bn2 = torch.nn.BatchNorm2d(8)
        self.bn3 = torch.nn.BatchNorm2d(8)
        self.bn4 = torch.nn.BatchNorm2d(8)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.bn1(v1)
        v3 = self.conv1(v2)
        v4 = self.bn2(v3)
        v5 = self.conv1(v4)
        v6 = self.bn3(v5)
        v7 = v6.add(self.bn4(v4))
        return v7



func = Model().to('cpu')


x = torch.randn(1, 8, 32, 32)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (10) at non-singleton dimension 3

jit:
Failed running call_method add(*(FakeTensor(...,
           size=(1, 8, ((((((s1 + 1)//4)) + 3)//2)) + 1, ((((((s2 + 1)//4)) + 3)//2)) + 1)), FakeTensor(..., size=(1, 8, (((s1 + 1)//4)) + 2, (((s2 + 1)//4)) + 2))), **{}):
The size of tensor a (((((((s2 + 1)//4)) + 3)//2)) + 1) must match the size of tensor b ((((s2 + 1)//4)) + 2) at non-singleton dimension 3)

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''