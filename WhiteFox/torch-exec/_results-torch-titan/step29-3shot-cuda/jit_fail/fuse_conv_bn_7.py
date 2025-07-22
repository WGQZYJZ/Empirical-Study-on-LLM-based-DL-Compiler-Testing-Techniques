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
        self.conv1 = torch.nn.Conv2d(1, 10, 10, 2, 1)
        self.conv2 = torch.nn.Conv2d(10, 10, 10, 2, 1)
        self.conv3 = torch.nn.Conv2d(10, 10, 10, 2, 1)
        self.relu1 = torch.nn.ReLU()
        self.relu2 = torch.nn.ReLU()
        self.relu3 = torch.nn.ReLU()
        self.layer1 = torch.nn.Sequential(self.conv1, self.relu1)
        self.layer2 = torch.nn.Sequential(self.conv2, self.relu2)
        self.layer3 = torch.nn.Sequential(self.conv3, self.relu3)

    def forward(self, input):
        out1 = self.layer1(input)
        out2 = self.layer2(input)
        out3 = self.layer3(input)
        outs = [out1, out2, out3]
        return outs




func = Model().to('cuda')



x1 = torch.randn(10, 1, 112, 112)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [10, 10, 10, 10], expected input[10, 1, 112, 112] to have 10 channels, but got 1 channels instead

jit:
Failed running call_module L__self___layer2_0(*(FakeTensor(..., device='cuda:0', size=(10, 1, 112, 112)),), **{}):
Given groups=1, weight of size [10, 10, 10, 10], expected input[10, 1, 112, 112] to have 10 channels, but got 1 channels instead

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''