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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.norm = torch.nn.BatchNorm2d(num_features=8, track_running_stats=True)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.norm(v1)
        v3 = self.norm(v2)
        v4 = self.norm(v3)
        w_tanh = torch.nn.Tanh(v4)
        return w_tanh



func = Model().to('cuda')



inputData = torch.randn(2, 4, 16, 16)


test_inputs = [inputData]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 1, 1], expected input[2, 4, 16, 16] to have 3 channels, but got 4 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(2, 4, 16, 16)),), **{}):
Given groups=1, weight of size [8, 3, 1, 1], expected input[2, 4, 16, 16] to have 3 channels, but got 4 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''