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
        self.conv3 = torch.nn.Conv2d(3, 6, kernel_size=3, stride=2, padding=1)
        self.conv1 = torch.nn.Conv2d(3, 6, kernel_size=1, stride=1, padding=0, dilation=1)

    def forward(self, x):
        x = self.conv3(x)
        x = self.conv1(x)
        x = (x - 4.2e-05)
        return x




func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [6, 3, 1, 1], expected input[1, 6, 32, 32] to have 3 channels, but got 6 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 6, 32, 32)),), **{}):
Given groups=1, weight of size [6, 3, 1, 1], expected input[1, 6, 32, 32] to have 3 channels, but got 6 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''