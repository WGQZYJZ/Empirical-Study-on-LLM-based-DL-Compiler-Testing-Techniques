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
        self.conv1 = torch.nn.Conv2d(24, 1, 3, stride=1, padding=1)

    def forward(self, x1):
        t0 = torch.zeros_like(x1)
        v1 = self.conv1(t0)
        v2 = (v1 - 0.5)
        v3 = F.relu(v2)
        return (v3 ** 0.5)




func = Model().to('cuda')



x1 = torch.randn(1, 1, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 24, 3, 3], expected input[1, 1, 32, 32] to have 24 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 1, 32, 32)),), **{}):
Given groups=1, weight of size [1, 24, 3, 3], expected input[1, 1, 32, 32] to have 24 channels, but got 1 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''