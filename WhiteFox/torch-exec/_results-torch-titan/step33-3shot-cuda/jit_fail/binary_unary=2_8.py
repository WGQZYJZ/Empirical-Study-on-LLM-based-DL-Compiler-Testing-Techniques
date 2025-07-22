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
        self.conv1 = torch.nn.Conv2d(3, 20, 5, stride=1, padding=2)
        self.conv2 = torch.nn.Conv2d(20, 50, 5, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1.transpose((- 1), (- 2))
        v3 = (v2 - 10)
        v4 = F.relu(v3)
        v5 = v4.transpose((- 1), (- 2))
        v6 = (v5 + 1)
        v7 = self.conv2(v6)
        v8 = (v7 - 11)
        v9 = F.relu(v8)
        v10 = self.conv2(v9)
        v11 = (v10 + 1)
        v12 = F.relu(v11)
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [50, 20, 5, 5], expected input[1, 50, 64, 64] to have 20 channels, but got 50 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 50, 64, 64)),), **{}):
Given groups=1, weight of size [50, 20, 5, 5], expected input[1, 50, 64, 64] to have 20 channels, but got 50 channels instead

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''