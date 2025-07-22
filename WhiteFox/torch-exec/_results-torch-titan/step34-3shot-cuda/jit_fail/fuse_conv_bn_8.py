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
        self.conv1 = torch.nn.Conv2d(3, 3, 4)
        self.batchnorm2d = torch.nn.BatchNorm2d(3)
        self.dropout = torch.nn.Dropout()

    def forward(self, x1, x2):
        s = torch.cat([x1, x2], dim=1)
        s = self.conv1(s)
        s = self.batchnorm2d(s)
        s = self.dropout(s)
        return s




func = Model().to('cuda')



x1 = torch.rand(1, 3, 6, 6)



x2 = torch.rand(1, 3, 6, 6)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 3, 4, 4], expected input[1, 6, 6, 6] to have 3 channels, but got 6 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 6, 6, 6)),), **{}):
Given groups=1, weight of size [3, 3, 4, 4], expected input[1, 6, 6, 6] to have 3 channels, but got 6 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''