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
        self.conv = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = v2.flatten(1, -1)
        v4 = v3.transpose(0, 1)
        v5 = v4.permute(1, 2, 0)
        v6 = torch.cat([v4, v5], dim=1)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 16, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 2 is not equal to len(dims) = 3

jit:
Failed running call_method permute(*(FakeTensor(..., size=(65536, 1)), 1, 2, 0), **{}):
Dimension out of range (expected to be in range of [-2, 1], but got 2)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''