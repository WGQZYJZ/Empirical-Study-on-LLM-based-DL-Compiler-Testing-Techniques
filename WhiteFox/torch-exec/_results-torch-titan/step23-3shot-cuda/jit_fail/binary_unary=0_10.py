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
        self.conv1 = torch.nn.Conv2d(36, 40, 1, stride=1, padding=0)

    def forward(self, x):
        v1 = self.conv1(x)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [40, 36, 1, 1], expected input[1, 16, 64, 64] to have 36 channels, but got 16 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64)),), **{}):
Given groups=1, weight of size [40, 36, 1, 1], expected input[1, 16, 64, 64] to have 36 channels, but got 16 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''