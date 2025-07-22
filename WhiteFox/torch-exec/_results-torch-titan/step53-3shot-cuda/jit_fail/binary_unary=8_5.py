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
        self.conv1 = torch.nn.Conv2d(16, 1, 3, stride=2, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 1, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv1(x1)
        v3 = self.conv1(x1)
        v4 = self.conv2(x1)
        v5 = ((((v4 + v4) + v4) + v4) + v4)
        v6 = torch.relu(v5)
        return ((v1 + v2) + v3)




func = Model().to('cuda')



x1 = torch.randn(1, 16, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 8, 1, 1], expected input[1, 16, 224, 224] to have 8 channels, but got 16 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 16, 224, 224)),), **{}):
Given groups=1, weight of size [1, 8, 1, 1], expected input[1, 16, 224, 224] to have 8 channels, but got 16 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''