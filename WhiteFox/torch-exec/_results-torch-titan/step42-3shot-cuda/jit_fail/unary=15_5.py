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
        self.conv1 = torch.nn.Conv2d(3, 16, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1, groups=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = torch.transpose(v2, 1, 0)
        v4 = torch.transpose(v2, 1, 3)
        v32 = self.conv2(v3)
        v42 = self.conv2(v4)
        v33 = torch.transpose(v32, 0, 2)
        v43 = torch.transpose(v42, 0, 2)
        v5 = torch.cat([v33, v43], 0)
        v6 = torch.relu(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=2, weight of size [16, 8, 3, 3], expected input[16, 1, 224, 224] to have 16 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(16, 1, 224, 224)),), **{}):
Given groups=2, weight of size [16, 8, 3, 3], expected input[16, 1, 224, 224] to have 16 channels, but got 1 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''