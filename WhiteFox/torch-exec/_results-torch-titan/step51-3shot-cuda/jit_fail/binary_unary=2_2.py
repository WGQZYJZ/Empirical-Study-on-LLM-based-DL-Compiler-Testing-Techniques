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
        super(Model, self).__init__()
        self.conv1 = torch.nn.Conv2d(14, 64, (1, 1), stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(64, 64, (1, 1), stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(64, 1, (1, 1), stride=1, padding=0)

    def forward(self, x):
        x1 = self.conv1(x)
        x2 = torch.transpose(x, 1, 2).contiguous()
        x3 = self.conv2(x2)
        x4 = torch.transpose(x3, 1, 2).contiguous()
        x5 = self.conv3(x4)
        return x5




func = Model().to('cuda')



x1 = torch.randn(1, 14, 20, 20)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 64, 1, 1], expected input[1, 20, 14, 20] to have 64 channels, but got 20 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 20, 14, 20)),), **{}):
Given groups=1, weight of size [64, 64, 1, 1], expected input[1, 20, 14, 20] to have 64 channels, but got 20 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''