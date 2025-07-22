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

    def __init__(self, N):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 100, 1)
        self.bn = torch.nn.BatchNorm2d(100)
        for _ in range(1, N):
            self.conv += torch.nn.Conv2d(100, 100, 1)
        self.fc = torch.nn.Linear((105 * 137), 1000)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x).relu()
        return self.fc(x.view(1, (- 1)))



N = 1

func = Model(N).to('cuda')



x = torch.randn(1, 1, 128, 127)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1625600 and 14385x1000)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(1, 1625600)),), **{}):
a and b must have same reduction dim, but got [1, 1625600] X [14385, 1000].

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''