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
        self.conv1 = torch.nn.Conv2d(16, 16, [1, 3, 3, 7], stride=[1, 1, 4, 1], padding=[1, 0, 0, 0])
        self.conv2 = torch.nn.Conv2d(16, 16, [1, 5, 1, 21], stride=[1, 1, 4, 1], padding=[1, 2, 0, 0])
        self.conv3 = torch.nn.Conv2d(16, 16, [1, 7, 7, 5], stride=[1, 1, 4, 1], padding=[1, 0, 0, 0])

    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = (v2 + x3)
        v4 = torch.relu(v3)
        v5 = self.conv3(v4)
        v6 = (x3 + v2)
        v7 = torch.relu(v6)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 16, 86, 64)



x3 = torch.randn(1, 16, 64, 64)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
expected dilation to be a single integer value or a list of 4 values to match the convolution dimensions, but got dilation=[1, 1]

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64)),), **{}):
expected dilation to be a single integer value or a list of 4 values to match the convolution dimensions, but got dilation=[1, 1]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''