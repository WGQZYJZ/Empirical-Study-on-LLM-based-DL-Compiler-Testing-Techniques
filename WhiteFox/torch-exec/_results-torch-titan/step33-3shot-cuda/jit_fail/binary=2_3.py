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
        self.conv1 = torch.nn.Conv2d(32, 3, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(32, 3, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = (v2 - 0.78)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 32, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 32, 1, 1], expected input[1, 3, 34, 34] to have 32 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 34, 34)),), **{}):
Given groups=1, weight of size [3, 32, 1, 1], expected input[1, 3, 34, 34] to have 32 channels, but got 3 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''