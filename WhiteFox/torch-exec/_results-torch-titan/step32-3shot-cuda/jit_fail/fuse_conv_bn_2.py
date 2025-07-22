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
        self.conv1 = torch.nn.Conv2d(1, 2, 2)
        torch.manual_seed(1)
        self.bn = torch.nn.BatchNorm2d(2)

    def forward(self, x):
        x1 = torch.nn.functional.relu(self.conv1(x))
        y1 = self.bn(x1)
        x2 = torch.nn.functional.relu(self.conv1(y1))
        y2 = self.bn(x2)
        return y2




func = Model().to('cuda')



x = torch.randn(1, 1, 4, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 1, 2, 2], expected input[1, 2, 3, 3] to have 1 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3, 3)),), **{}):
Given groups=1, weight of size [2, 1, 2, 2], expected input[1, 2, 3, 3] to have 1 channels, but got 2 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''