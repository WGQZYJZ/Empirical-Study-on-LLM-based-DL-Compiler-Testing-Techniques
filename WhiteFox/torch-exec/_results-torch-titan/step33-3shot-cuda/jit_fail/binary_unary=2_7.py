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
        self.conv1 = torch.nn.Conv2d(3, 20, 5, stride=2, padding=2)
        self.conv2 = torch.nn.Conv2d(20, 50, 5, stride=2, padding=2)
        self.conv3 = torch.nn.ConvTranspose2d(50, 20, 5, stride=2, padding=2)
        self.conv4 = torch.nn.ConvTranspose2d(20, 1, 5, stride=2, padding=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(280, 1, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [20, 3, 5, 5], expected input[280, 1, 28, 28] to have 3 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(280, 1, 28, 28)),), **{}):
Given groups=1, weight of size [20, 3, 5, 5], expected input[280, 1, 28, 28] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''