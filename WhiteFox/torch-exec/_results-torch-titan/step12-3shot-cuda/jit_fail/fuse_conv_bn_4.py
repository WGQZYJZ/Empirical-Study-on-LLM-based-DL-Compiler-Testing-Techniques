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
        self.conv3 = torch.nn.Conv3d(2, 2, 3)
        self.bn3 = torch.nn.BatchNorm3d(2)
        self.c1 = torch.nn.Conv3d(2, 3, 3)
        self.c2 = torch.nn.Conv3d(3, 4, 3)
        self.bn1 = torch.nn.BatchNorm3d(4)
        self.bn2 = torch.nn.BatchNorm3d(5)

    def forward(self, x3):
        x3 = self.conv3(x3)
        y1 = self.bn3(x3)
        y1 = self.c1(y1)
        y2 = self.c2(y1)
        y2 = self.bn1(y2)
        return self.bn2(y2)




func = Model().to('cuda')



x3 = torch.randn(1, 2, 4, 4, 4)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 2 x 2). Kernel size: (3 x 3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___c1(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2, 2)),), **{}):
Calculated padded input size per channel: (2 x 2 x 2). Kernel size: (3 x 3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''