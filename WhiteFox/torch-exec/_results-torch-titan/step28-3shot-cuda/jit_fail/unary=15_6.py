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
        self.conv1 = torch.nn.Conv2d(11, 24, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(28, 81, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 11, 128, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [81, 28, 1, 1], expected input[1, 24, 130, 130] to have 28 channels, but got 24 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 24, 130, 130)),), **{}):
Given groups=1, weight of size [81, 28, 1, 1], expected input[1, 24, 130, 130] to have 28 channels, but got 24 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''