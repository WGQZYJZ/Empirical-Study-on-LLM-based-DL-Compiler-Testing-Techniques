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
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.conv2 = torch.nn.Conv2d(16, 4, 1, stride=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 - 10)
        v3 = F.relu(v2)
        v4 = F.avg_pool2d(v3, 2, stride=2, padding=0)
        v5 = self.conv2(v4)
        v6 = (v5 - 11)
        v7 = F.relu(v6)
        v8 = (v7 - 7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 16, 1, 1], expected input[1, 8, 111, 111] to have 16 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 8, 111, 111)),), **{}):
Given groups=1, weight of size [4, 16, 1, 1], expected input[1, 8, 111, 111] to have 16 channels, but got 8 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''