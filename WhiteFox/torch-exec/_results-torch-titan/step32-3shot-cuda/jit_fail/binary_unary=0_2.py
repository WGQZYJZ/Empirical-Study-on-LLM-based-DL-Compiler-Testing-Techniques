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
        self.conv = torch.nn.Conv2d(3, 8, 5, stride=2, padding=0)
        self.pool = torch.nn.MaxPool2d(kernel_size=3, stride=2, padding=0)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.relu(v1)
        v3 = self.conv(v2)
        v4 = torch.relu(v3)
        v6 = self.pool(v4)
        return v6




func = Model().to('cuda')



x = torch.randn(1, 3, 100, 100)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 5, 5], expected input[1, 8, 48, 48] to have 3 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 8, 48, 48)),), **{}):
Given groups=1, weight of size [8, 3, 5, 5], expected input[1, 8, 48, 48] to have 3 channels, but got 8 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''