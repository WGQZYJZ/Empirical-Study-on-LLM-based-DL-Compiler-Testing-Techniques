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
        self.downconvs = torch.nn.Sequential(*([torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1), torch.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1), torch.nn.Conv2d(in_channels=32, out_channels=48, kernel_size=3, padding=1)] * 2))

    def forward(self, x1):
        v1 = self.downconvs(x1)
        v2 = torch.nn.Sigmoid()(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 3, 3, 3], expected input[1, 48, 224, 224] to have 3 channels, but got 48 channels instead

jit:
Failed running call_module L__self___downconvs_0(*(FakeTensor(..., device='cuda:0', size=(1, 48, 224, 224)),), **{}):
Given groups=1, weight of size [16, 3, 3, 3], expected input[1, 48, 224, 224] to have 3 channels, but got 48 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''