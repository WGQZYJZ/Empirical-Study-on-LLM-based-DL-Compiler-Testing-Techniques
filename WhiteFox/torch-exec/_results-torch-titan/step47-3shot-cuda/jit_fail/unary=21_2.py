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
        self.conv = torch.nn.Conv2d(3, 32, 1)
        self.relu = torch.nn.ReLU()
        self.linear = torch.nn.Linear(in_features=32, out_features=64, bias=True)
        self.tanh = torch.nn.Tanh()

    def forward(self, z):
        w1 = self.conv(z)
        v3 = self.tanh(w1)
        g1 = self.linear(v3)
        u1 = self.relu(g1)
        v5 = self.tanh(u1)
        return v5




func = ModelTanh().to('cuda')



u = torch.randn(1, 3, 4, 4, requires_grad=True)


test_inputs = [u]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (128x4 and 32x64)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 32, 4, 4)),), **{}):
a and b must have same reduction dim, but got [128, 4] X [32, 64].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''