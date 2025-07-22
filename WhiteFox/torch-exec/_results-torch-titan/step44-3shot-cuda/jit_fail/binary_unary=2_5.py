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
        self.conv1 = torch.nn.Conv2d(8, 8, 5, stride=1, padding=0)

    def forward(self, x1):
        x1 = self.conv1(x1)
        x2 = (x1 - 0.75)
        x3 = F.relu(x2)
        x4 = self.conv1(x3)
        x5 = (x4 - 1)
        x6 = F.relu(x5)
        x7 = self.conv1(x6)
        x8 = (x7 + 0.25)
        x9 = F.relu(x8)
        return x9




func = Model().to('cuda')



x1 = torch.randn(1, 8, 12, 12)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (4 x 4). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 8, 4, 4)),), **{}):
Calculated padded input size per channel: (4 x 4). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''