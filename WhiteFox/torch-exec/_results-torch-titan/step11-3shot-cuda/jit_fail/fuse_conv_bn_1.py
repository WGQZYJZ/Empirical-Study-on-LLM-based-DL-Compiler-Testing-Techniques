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



class M(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 3, 3)
        self.conv2 = torch.nn.Conv2d(3, 3, 3)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        x1 = self.conv1(x1)
        y = self.bn(x1)
        y = self.bn(y)
        if (y.size(0) == 1):
            y = self.conv2(y)
        else:
            y = self.conv1(y)
        return y




func = M().to('cuda')



x1 = torch.randn(2, 1, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 1, 3, 3], expected input[2, 3, 2, 2] to have 1 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(2, 3, 2, 2)),), **{}):
Given groups=1, weight of size [3, 1, 3, 3], expected input[2, 3, 2, 2] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''