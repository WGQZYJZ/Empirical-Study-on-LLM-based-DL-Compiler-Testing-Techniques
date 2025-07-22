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
        self.conv = torch.nn.Conv2d(1, 1, 12, stride=3)
        self.flatten = torch.flatten
        self.linear = torch.nn.Linear(2, 10)
        self.conv_transpose = torch.nn.ConvTranspose2d(12, 24, 3, stride=3)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = torch.flatten(v2)
        v4 = self.linear(v3)
        v5 = torch.relu(v4)
        v6 = torch.sigmoid(v5)
        v7 = self.conv_transpose(v6)
        v8 = torch.tanh(v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 1, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x5041 and 2x10)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(5041,)),), **{}):
a and b must have same reduction dim, but got [1, 5041] X [2, 10].

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''