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
        self.conv1 = torch.nn.Conv2d(100, 300, 1)
        self.conv2 = torch.nn.Conv2d(300, 300, 1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        return v2




func = Model().to('cuda')



x = torch.randn(1, 100, 100)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [300, 100, 1, 1], expected input[1, 1, 100, 100] to have 100 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 100, 100)),), **{}):
Given groups=1, weight of size [300, 100, 1, 1], expected input[1, 1, 100, 100] to have 100 channels, but got 1 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''