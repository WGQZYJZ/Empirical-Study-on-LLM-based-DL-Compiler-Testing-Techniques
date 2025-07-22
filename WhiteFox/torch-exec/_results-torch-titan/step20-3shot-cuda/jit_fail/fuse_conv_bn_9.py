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
        self.conv1 = torch.nn.Conv1d(3, 3, 3)
        self.conv2 = torch.nn.Conv1d(3, 3, 3)
        self.bn = torch.nn.BatchNorm1d(3)

    def forward(self, x1):
        s = self.conv1(x1)
        t = self.conv2(s)
        y = self.bn(t)
        return s




func = Model().to('cuda')



x1 = torch.randn(1, 3, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2). Kernel size: (3). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 0)),), **{}):
Trying to create tensor with negative dimension -2: [1, 3, -2]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''