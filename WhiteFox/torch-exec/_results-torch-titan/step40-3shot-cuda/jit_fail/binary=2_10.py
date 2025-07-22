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
        self.conv1 = torch.nn.Conv2d(16, 32, 5, stride=2, padding=2)
        self.conv2 = torch.nn.Conv2d(16, 32, 5, stride=2, padding=2)
        self.conv3 = torch.nn.Conv2d(16, 32, 5, stride=2, padding=2)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(x)
        v3 = self.conv3(v1)
        v4 = (v3 - v2)
        return v4




func = Model().to('cuda')



x = torch.randn(1, 16, 28, 28)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 16, 5, 5], expected input[1, 32, 14, 14] to have 16 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1, 32, 14, 14)),), **{}):
Given groups=1, weight of size [32, 16, 5, 5], expected input[1, 32, 14, 14] to have 16 channels, but got 32 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''