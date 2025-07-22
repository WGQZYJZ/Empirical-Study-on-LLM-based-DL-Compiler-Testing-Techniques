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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=2)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=2)

    def forward(self, x1, other=None):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        if (other == None):
            other = torch.randn(v2.shape[1:])
        v3 = (v2 + other)
        return v3




func = Model().to('cuda')



x1 = torch.randn(5, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 1, 1], expected input[5, 8, 68, 68] to have 3 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(5, 8, 68, 68)),), **{}):
Given groups=1, weight of size [8, 3, 1, 1], expected input[5, 8, 68, 68] to have 3 channels, but got 8 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''