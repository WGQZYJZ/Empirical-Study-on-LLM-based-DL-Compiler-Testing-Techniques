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
        self.conv1 = torch.nn.Conv2d(3, 3, 1, 1, 0)
        self.conv2 = torch.nn.Conv2d(3, 16, 1, 1, 0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = v2.reshape((v2.shape[0], 16, (- 1)))
        v4 = v3.permute(0, 2, 1)
        v5 = self.conv2(v4)
        v6 = torch.sigmoid(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 3, 1, 1], expected input[1, 1, 768, 16] to have 3 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 768, 16)),), **{}):
Given groups=1, weight of size [16, 3, 1, 1], expected input[1, 1, 768, 16] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''