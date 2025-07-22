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
        self.conv1 = torch.nn.Conv2d(2, 3, 6, stride=7, padding=1)
        self.conv2 = torch.nn.Conv2d(5, 4, 6, stride=1, padding=0)

    def forward(self, x3):
        v1 = self.conv1(x3)
        v2 = self.conv2(v1)
        v3 = (v2 * 0.5)
        v4 = (v2 * v2)
        v5 = (v4 * v2)
        v6 = (v5 * 0.044715)
        v7 = (v2 + v6)
        v8 = (v7 * 0.7978845608028654)
        v9 = torch.tanh(v8)
        v10 = (v9 + 1)
        v11 = (v3 * v10)
        return v11




func = Model().to('cuda')



x3 = torch.randn(21, 5, 79, 88)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 2, 6, 6], expected input[21, 5, 79, 88] to have 2 channels, but got 5 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(21, 5, 79, 88)),), **{}):
Given groups=1, weight of size [3, 2, 6, 6], expected input[21, 5, 79, 88] to have 2 channels, but got 5 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''