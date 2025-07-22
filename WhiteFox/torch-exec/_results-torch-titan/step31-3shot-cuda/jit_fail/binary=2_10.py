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
        self.conv1 = torch.nn.Conv2d(1, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(2, 4, 3, stride=2, padding=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v3 = self.conv2(v1)
        v2 = (v3 - 0.0)
        return v2




func = Model().to('cuda')



x = torch.randn(1, 1, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 2, 3, 3], expected input[1, 8, 66, 66] to have 2 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)),), **{}):
Given groups=1, weight of size [4, 2, 3, 3], expected input[1, 8, 66, 66] to have 2 channels, but got 8 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''