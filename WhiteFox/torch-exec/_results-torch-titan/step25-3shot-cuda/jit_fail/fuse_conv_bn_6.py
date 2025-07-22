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
        self.conv1 = torch.nn.Conv3d(2, 2, 3)
        self.conv2 = torch.nn.Conv3d(2, 2, 3)
        self.bn = torch.nn.BatchNorm3d(2)
        self.relu = torch.nn.ReLU()

    def forward(self, x2):
        v2 = self.relu(self.bn(self.conv1(x2)))
        v2 = self.relu(self.bn(self.conv2(v2)))
        return v2




func = Model().to('cuda')



x2 = torch.randn(1, 2, 3, 4, 4)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 2 x 2). Kernel size: (3 x 3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 2, 1, 2, 2)),), **{}):
Calculated padded input size per channel: (1 x 2 x 2). Kernel size: (3 x 3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''