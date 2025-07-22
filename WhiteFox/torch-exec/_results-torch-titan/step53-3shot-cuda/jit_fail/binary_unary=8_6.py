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
        weight = torch.rand(4, 10)
        bias = torch.rand(4)
        self.conv1 = torch.nn.Conv1d(3, 4, 1)
        self.conv1.weight = torch.nn.Parameter(weight)
        self.conv1.bias = torch.nn.Parameter(bias)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 * v1)
        v3 = torch.relu(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
weight should have at least three dimensions

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 224)),), **{}):
Expected 2-dimensional input for 2-dimensional weight [4, 10], but got 3-dimensional input of size [1, 3, 224] instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''