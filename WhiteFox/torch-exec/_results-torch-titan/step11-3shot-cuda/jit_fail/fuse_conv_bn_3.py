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
        self.relu = torch.nn.ReLU()
        self.conv3 = torch.nn.Conv2d(1, 4, 3)
        self.bn1 = torch.nn.BatchNorm2d(4)

    def forward(self, x):
        x = self.conv3(x)
        x = self.bn1(x)
        x = self.relu(x)
        return x.sum()




func = Model().to('cuda')



x1 = torch.randn(1, 1, 1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 1). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1, 1)),), **{}):
Calculated padded input size per channel: (1 x 1). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''