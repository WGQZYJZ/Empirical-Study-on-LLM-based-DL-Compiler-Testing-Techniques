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
        self.conv = torch.nn.Conv2d(1, 32, 7, stride=1, padding=3)
        self.pool0 = torch.nn.MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, return_indices=False, ceil_mode=False)
        self.fc1 = torch.nn.Linear(8, 8)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 - 5)
        v3 = F.relu(v2)
        v4 = self.pool0(v3)
        v5 = v4.flatten(start_dim=1)
        v6 = self.fc1(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 1, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x6272 and 8x8)

jit:
Failed running call_module L__self___fc1(*(FakeTensor(..., device='cuda:0', size=(1, 6272)),), **{}):
a and b must have same reduction dim, but got [1, 6272] X [8, 8].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''