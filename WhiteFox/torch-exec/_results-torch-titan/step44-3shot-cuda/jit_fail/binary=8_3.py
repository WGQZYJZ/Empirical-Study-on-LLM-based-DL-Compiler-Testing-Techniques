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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv5 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv6 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv7 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)

    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v4 = self.conv4(x3)
        v3 = torch.cat((v1, v2, v4))
        v5 = self.conv3(x1)
        v6 = self.conv5(x2)
        v7 = self.conv7(x3)
        v8 = torch.cat((v5, v6, v7))
        v9 = self.conv6((v3 + v8))
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)



x2 = torch.randn(1, 3, 32, 32)



x3 = torch.randn(1, 3, 32, 32)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 1, 1], expected input[3, 8, 17, 17] to have 3 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv6(*(FakeTensor(..., device='cuda:0', size=(3, 8, 17, 17)),), **{}):
Given groups=1, weight of size [8, 3, 1, 1], expected input[3, 8, 17, 17] to have 3 channels, but got 8 channels instead

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''