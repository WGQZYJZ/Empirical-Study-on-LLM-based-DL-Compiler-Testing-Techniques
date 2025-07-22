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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v2 = self.conv1(x2)
        with torch.no_grad():
            v3 = self.conv1(x3)
        v4 = torch.mean(v3, dim=((- 1), (- 2)))
        v5 = torch.mean(v3, dim=((- 2), (- 1)))
        v6 = v3.view(x1.shape[0], 1, (- 1))
        v7 = self.conv2(v6)
        v8 = (v7 + v1)
        v9 = self.conv3(v8)
        v10 = self.conv3(v9)
        v11 = (v10 + v4)
        return v11




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 16, 64, 64)



x3 = torch.randn(2, 16, 64, 64)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 16, 7, 7], expected input[1, 1, 1, 131072] to have 16 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 1, 131072)),), **{}):
Given groups=1, weight of size [16, 16, 7, 7], expected input[1, 1, 1, 131072] to have 16 channels, but got 1 channels instead

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''