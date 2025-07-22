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
        self.conv1 = torch.nn.Conv2d(3, 64, 5)
        self.bn = torch.nn.BatchNorm2d(3)
        self.conv2 = torch.nn.Conv2d(64, 128, 5)
        self.relu = torch.nn.ReLU(True)
        self.conv3 = torch.nn.Conv2d(128, 128, 7)

    def forward(self, x):
        conv1 = self.conv1(x)
        bn = self.bn(conv1)
        conv2 = self.conv2(self.relu(bn))
        conv3 = self.conv3(self.relu(conv2))
        return conv3




func = Model().to('cuda')



x = torch.randn(1, 3, 32, 32)


test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 64 elements not 3

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(1, 64, 28, 28)),), **{}):
running_mean should contain 64 elements not 3

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''