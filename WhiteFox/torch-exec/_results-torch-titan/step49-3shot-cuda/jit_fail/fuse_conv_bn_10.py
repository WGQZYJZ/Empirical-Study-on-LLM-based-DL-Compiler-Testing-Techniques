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
        self.conv = torch.nn.Conv2d(3, 3, 3)
        self.bn1 = torch.nn.BatchNorm2d(3)
        self.bn2 = torch.nn.BatchNorm2d(3)
        self.conv2 = torch.nn.Conv2d(3, 1, 1)
        self.softmax = torch.nn.Softmax(dim=1)
        self.drop = torch.nn.Dropout(0.5)

    def forward(self, x1):
        s = self.conv(x1)
        t1 = self.bn1(s)
        t2 = self.conv(s)
        t2 = self.bn2(t2)
        y1 = self.conv2(t1)
        y2 = self.conv2(t2)
        self.drop(y1)
        self.drop(y2)
        self.softmax(y1)
        self.softmax(y2)
        return (y1, y2)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 2, 2)),), **{}):
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''