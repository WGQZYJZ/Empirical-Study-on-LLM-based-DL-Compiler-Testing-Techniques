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
        self.conv = torch.nn.Conv2d(3, 4, 0, stride=1)
        self.conv2 = torch.nn.Conv2d(4, 4, 1, stride=1, padding=1)

    def forward(self, x1):
        x2 = torch.zeros_like(x1)
        v1 = self.conv(x1)
        v2 = self.conv2(x2)
        v3 = ((v2 * v2) == 0)
        v4 = (v1 + v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
CUDNN_BACKEND_OPERATION: cudnnFinalize Failed cudnn_status: CUDNN_STATUS_BAD_PARAM

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
Given groups=1, weight of size [4, 4, 1, 1], expected input[1, 3, 64, 64] to have 4 channels, but got 3 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''