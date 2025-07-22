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
        self.conv1 = torch.nn.Conv2d(4, 12, 3)
        self.conv2 = torch.nn.Conv2d(24, 12, 1)
        self.bn = torch.nn.BatchNorm2d(12)
        torch.manual_seed(9)
        self.conv1.weight = torch.nn.Parameter(torch.randn(self.conv1.weight.shape))
        self.conv2.weight = torch.nn.Parameter(torch.randn(self.conv2.weight.shape))
        torch.manual_seed(10)
        self.conv1.bias = torch.nn.Parameter(torch.randn(self.conv1.bias.shape))
        self.conv2.bias = torch.nn.Parameter(torch.randn(self.conv2.bias.shape))

    def forward(self, x1, x2):
        out1 = self.conv1(x1)
        torch.manual_seed(11)
        out2 = torch.nn.functional.pad(out1, (23, 7, 20, 2, 3, 1))
        torch.manual_seed(12)
        y = self.conv2(out2)
        return self.bn(y)




func = Model().to('cuda')



x1 = torch.randn(1, 4, 10, 10)



x2 = torch.randn(1, 24, 6, 6)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [12, 24, 1, 1], expected input[1, 16, 30, 38] to have 24 channels, but got 16 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 16, 30, 38)),), **{}):
Given groups=1, weight of size [12, 24, 1, 1], expected input[1, 16, 30, 38] to have 24 channels, but got 16 channels instead

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''