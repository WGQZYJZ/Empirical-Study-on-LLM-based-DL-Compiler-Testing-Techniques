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



class PatternModule(torch.nn.Module):

    def __init__(self):
        super(PatternModule, self).__init__()
        self.conv3x3 = torch.nn.Conv2d(32, 128, 3, stride=1, padding=1)
        self.conv1x1 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)

    def forward(self, inputs):
        conv3x3_inputs = self.conv3x3(inputs)
        conv1x1_inputs = self.conv1x1(inputs)
        concat_outputs = torch.cat([conv3x3_inputs, conv1x1_inputs], dim=params.Dim.CHANNEL_DIM)
        return concat_outputs




func = PatternModule().to('cuda')



inputs = torch.randn(2, 32, 64, 64)


test_inputs = [inputs]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 64, 1, 1], expected input[2, 32, 64, 64] to have 64 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv1x1(*(FakeTensor(..., device='cuda:0', size=(2, 32, 64, 64)),), **{}):
Given groups=1, weight of size [64, 64, 1, 1], expected input[2, 32, 64, 64] to have 64 channels, but got 32 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''