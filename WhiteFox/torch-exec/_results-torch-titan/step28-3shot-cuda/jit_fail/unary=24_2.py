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
        self.conv1 = torch.nn.Conv2d(1, 16, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(16, 64, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(64, 20, 1, stride=1, padding=0)
        self.dropout1 = torch.nn.Dropout(p=0.2)
        self.dropout2 = torch.nn.Dropout(p=0.1)
        self.dropout3 = torch.nn.Dropout(p=0.3)
        self.linear1 = torch.nn.Linear(20, 64)

    def forward(self, x):
        negative_slope = 0.45
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = (v3 > 0)
        v5 = (v3 * negative_slope)
        v6 = torch.where(v4, v3, v5)
        v7 = self.dropout1(v6)
        v8 = self.linear1(v7)
        v9 = self.dropout2(v8)
        v10 = self.dropout3(v9)
        v11 = self.linear1(v10)
        return v11




func = Model().to('cuda')



x1 = torch.randn(2, 1, 128, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5120x128 and 20x64)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(2, 20, 128, 128)),), **{}):
a and b must have same reduction dim, but got [5120, 128] X [20, 64].

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''