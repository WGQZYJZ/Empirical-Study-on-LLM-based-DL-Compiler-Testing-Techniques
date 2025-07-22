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
        self.conv1 = torch.nn.Conv2d(3, 4, 2)
        self.conv2 = torch.nn.Conv2d(3, 5, 2)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        s = self.conv1(x1)
        t = self.conv2(s)
        y = self.bn(t)
        return y




func = Model().to('cuda')



x1 = torch.rand(1, 3, 6, 6)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [5, 3, 2, 2], expected input[1, 4, 5, 5] to have 3 channels, but got 4 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 4, 5, 5)),), **{}):
Given groups=1, weight of size [5, 3, 2, 2], expected input[1, 4, 5, 5] to have 3 channels, but got 4 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''